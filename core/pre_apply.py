from rest_framework.views import APIView, Response
from core.serializer import *
from core.forms import *
from core.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404


class PredictionStudentListView(APIView):
    """get:获取预报名学生列表"""
    """post:新建预报名"""

    def get(self, request):
        user_id = request.GET.get('user_id')
        user = User.objects.filter(id=int(user_id)).first()
        page = int(request.GET.get('page'))

        print(page)
        if user.role == '3':
            # print(1111)
            student = Student.objects.filter(user_id=user)
            seriz = PredictionListSerializer(student, many=True)
            # print(seriz.data)
            return Response({'data': seriz.data, 'result': '1', 'message': '获取成功'})
        if user.role in ['1', '2']:
            sex = request.GET.get('sex')
            major = request.GET.get('major')
            department = request.GET.get('department')
            academy = request.GET.get('academy')
            location = request.GET.get('location')
            condition = {
            }
            if sex:
                condition['sex'] = sex
            if major:
                condition['major'] = major
            if department:
                condition['department'] = department
            if academy:
                condition['academy'] = academy
            if location:
                condition['location'] = location
            students = Student.objects.filter(**condition).order_by('-id')[(page - 1) * 10:(page - 1) * 10 + 10]
            count = Student.objects.filter(**condition).count()
            seriz = PredictionListSerializer(students, many=True)
            return Response({'data': seriz.data, 'result': '1', 'message': '获取成功', 'count': count})
        return Response({'result': '0', 'message': '非用户不可查看'})

    def post(self, request):
        user_id = request.data.get('user_id')
        if not user_id:
            return Response({'result': '0', 'message': '缺少user_id'})
        user = User.objects.filter(id=int(user_id)).first()
        if not user:
            return Response({'result': '0', 'message': '该用户不存在'})
        form = StudentForm(request.data)
        print(form.errors)
        if form.is_valid():
            data = form.cleaned_data
            try:
                student = Student.objects.create(name=data['name'], sex=data['sex'],
                                                 age=data['age'],
                                                 major=data['major'],
                                                 department=data['department'],
                                                 academy=data['academy'],
                                                 location=data['location'],
                                                 user_id=user,
                                                 )
            except:
                return Response({'result': '0', 'message': '创建失败'})
            return Response({'result': '1', 'message': '创建成功', 'data': {'student_record_id': student.id}})
        return Response({'result': '0', 'message': '数据不完整'})


class PredictionStudentDetailView(APIView):
    """get:查看学生详细信息"""
    """put:修改学生信息"""

    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except ObjectDoesNotExist:
            raise Http404

    def get(self, request, pk):
        user_id = request.GET.get('id')
        if not user_id:
            return Response({'result': '0', 'message': '缺少user_id'})
        user = User.objects.filter(id=int(user_id)).first()
        if not user:
            return Response({'result': '0', 'message': '该用户不存在'})
        student = self.get_object(pk)
        print(student)
        seriz = PredictionListSerializer(student)
        print(seriz.data)
        return Response({'data': seriz.data, 'result': '1', 'message': '获取成功'})

    def put(self, request, pk):
        user_id = request.data.get('user_id')
        print(user_id)
        if not user_id:
            return Response({'result': '0', 'message': '缺少user_id'})
        user = User.objects.filter(id=int(user_id)).first()
        if not user:
            return Response({'result': '0', 'message': '该用户不存在'})
        if user.role == '3':
            student = Student.objects.filter(id=pk).first()
            form = StudentForm(request.data)
            print(form.errors)
            if form.is_valid():
                data = form.cleaned_data
                student.name = data['name']
                student.age = data['age']
                student.academy = data['academy']
                student.major = data['major']
                student.location = data['location']
                student.department = data['department']
                student.sex = data['sex']
                student.save()
                return Response({'result': '1', 'message': '修改成功'})
            return Response({'result': '0', 'message': '数据不完整'})
        return Response({'result': '0', 'message': '该用户无此权限'})


    def delete(self, request, pk):
        user_id = request.data.get('user_id')
        if not user_id:
            return Response({'result': '0', 'message': '缺少user_id'})
        user = User.objects.filter(id=int(user_id)).first()
        if not user:
            return Response({'result': '0', 'message': '该用户不存在'})
        land = self.get_object(pk)
        land.delete()
        return Response({'result': '1', 'message': '删除成功'})
