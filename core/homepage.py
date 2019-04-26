from rest_framework.views import APIView, Response
from core.serializer import *
from core.forms import *
from core.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
import json


class FiveView(APIView):

    def get(self, request):
        user_id = request.GET.get('user_id', 1)
        if not user_id:
            return Response({'result': '0', 'message': '缺少user_id'})
        user = User.objects.filter(id=int(user_id)).first()
        if not user:
            return Response({'result': '0', 'message': '该用户不存在'})
        city = request.GET.get('city')
        page = int(request.GET.get('page', 1))
        condition = {}
        year = []
        peo_five = []
        five_count = {}
        department = []
        peo_top = []
        top_ten_count = {}
        # 获取近五年学生人数，并根据年份排序
        five_years = FiveYears.objects.all().order_by('year')
        for i in five_years:
            year.append(i.year)
            peo_five.append(i.peo_count)
        five_count['year'] = year
        five_count['peo_count'] = peo_five
        # 获取专业前10，并根据人数排序
        topten = TopTen.objects.all().order_by('-peo_count')[0:10]
        for j in topten:
            department.append(j.department)
            peo_top.append(j.peo_count)
        top_ten_count['department'] = department
        top_ten_count['peo_top'] = peo_top
        # 取出所有的市名
        team = Team.objects.all()
        city_data = {}
        citys = []
        for c in team:
            if c.city in citys:
                pass
            else:
                citys.append(str(c.city))
        city_data['citys'] = citys
        if city:
            condition['city'] = city
        # print(city)
        teams = Team.objects.filter(**condition).order_by('-id')[(page - 1) * 5:(page - 1) * 5 + 5]
        print(type(teams))
        data_teachers = {}
        for team in teams:
            teachers = Teacher.objects.filter(team_id=team.id)
            teacher_list = []
            for teacher in teachers:
                # print(dict(teacher))
                teacher_info = {'name':teacher.name, 'sex':teacher.sex}
                teacher_list.append(teacher_info)

            data_teachers[team.name] = teacher_list
        count = Team.objects.filter(**condition).count()
        team_data = TeamSerializer(teams, many=True)
        return Response({'data_year_count': five_count,
                         'city_data': city_data,
                         'data_top_ten_count': top_ten_count,
                         'team_data': team_data.data,
                         'data_teachers': data_teachers,
                         'count': count,
                         'result': '1', 'message': '获取成功'})
