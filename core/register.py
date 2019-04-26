from rest_framework.views import APIView, Response
from core.models import *


class Register(APIView):
    def post(self, request):
        name = request.data.get('name')
        pwd = request.data.get('pwd')
        pwd2 = request.data.get('pwd2')
        role = request.data.get('role')
        print(name)
        if name and role and pwd == pwd2:
            role = Role.objects.create(name=role)
            user = User.objects.create(name=name, pwd=pwd, role_id=role)
            return Response({'result': '1', 'data': user, 'message': '注册成功'})
        return Response({'result': '0', 'message': '格式不正确'})
