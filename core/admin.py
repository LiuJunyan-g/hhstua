from django.contrib import admin
from core.models import *


# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'pwd', 'role')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', "name", "sex", "age", "major", "department", "academy", "location", "user_id")


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', "name", "sex", "age", "department", "academy", "user_id", "team_id")



@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city', 'county')


@admin.register(FiveYears)
class FiveAdmin(admin.ModelAdmin):
    list_display = ('id', 'peo_count', 'year')


@admin.register(TopTen)
class TopTenAdmin(admin.ModelAdmin):
    list_display = ('id', 'peo_count', 'department')
