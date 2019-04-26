from django.db import models


# Create your models here.


ROLE_CHOICES = [
    ('1', '校长'),
    ('2', '老师'),
    ('3', '学生')
]


class User(models.Model):
    name = models.CharField('用户名', max_length=16, null=True)
    pwd = models.CharField('密码', max_length=36, null=True)
    role = models.CharField('角色', choices=ROLE_CHOICES,  max_length=2, default='1')

    class Meta:
        verbose_name_plural = '用户表'
        verbose_name = '用户'

    def __str__(self):
        return self.name


class Student(models.Model):
    create_on = models.DateTimeField('创建时间', auto_now_add=True, null=True, blank=True)
    name = models.CharField('姓名', max_length=16, null=True)
    sex = models.CharField('性别', max_length=4)
    age = models.CharField('年龄', max_length=16, null=True)
    major = models.CharField('专业', max_length=64, null=True)
    department = models.CharField('系', max_length=64, null=True)
    academy = models.CharField('院', max_length=64, null=True)
    location = models.CharField('所在地', max_length=128, null=True)
    user_id = models.ForeignKey('User', verbose_name='用户', related_name='students',
                                on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name_plural = '学生表'
        verbose_name = '学生'

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField('团队名称', max_length=64, null=True)
    city = models.CharField('市', max_length=16, null=True)
    county = models.CharField('县', max_length=16, null=True)

    class Meta:
        verbose_name_plural = '团队表'
        verbose_name = '团队'


class Teacher(models.Model):
    create_on = models.DateTimeField('创建时间', auto_now_add=True, null=True, blank=True)
    name = models.CharField('姓名', max_length=16, null=True)
    sex = models.CharField('性别', max_length=4,)
    age = models.CharField('年龄', max_length=16, null=True)
    department = models.CharField('系', max_length=64, null=True)
    academy = models.CharField('院', max_length=64, null=True)
    user_id = models.ForeignKey('User', verbose_name='用户', related_name='teachers',
                                on_delete=models.CASCADE, null=True, blank=True)
    team_id = models.ForeignKey('Team', verbose_name='团队', related_name='teachers',
                                on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name_plural = '教师表'
        verbose_name = '教师'



class FiveYears(models.Model):
    peo_count = models.IntegerField('人数')
    year = models.IntegerField('年份')


class TopTen(models.Model):
    peo_count = models.IntegerField('人数')
    department = models.CharField('专业', max_length=64)
