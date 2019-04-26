from django.urls import path
from core.login import *
from core.register import *
from core.pre_apply import *
from core.homepage import *
app_name = 'jiangqiao'
urlpatterns = [
    # 登录
    path('login/', LoginView.as_view()),
    # 注册
    path('register/', Register.as_view()),
    # 首页
    path('getinfo_admission/', FiveView.as_view()),
    # 获取预报名列表页
    path('get_students/', PredictionStudentListView.as_view()),
    # 新建学生
    path('create_student/', PredictionStudentListView.as_view()),
    # 更改学生
    path('update_student_detail/<int:pk>/', PredictionStudentDetailView.as_view()),
    # 删除学生
    path('delete_student_detail/<int:pk>/', PredictionStudentDetailView.as_view()),

]