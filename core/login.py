from rest_framework.views import APIView, Response
from core.models import *
from core.serializer import *


class LoginView(APIView):

    def post(self, request):
        name = request.data.get('name')
        pwd = request.data.get('pwd')
        print(name)
        print(pwd)
        user = User.objects.filter(name=name).first()
        if user:
            if pwd == user.pwd:
                seriz = LoginSerializer(user)
                print(seriz.data)
                return Response({'result': '1', 'data': seriz.data, 'message': '登录成功'})
        return Response({'result': '0', 'message': '用户名或密码错误'})
