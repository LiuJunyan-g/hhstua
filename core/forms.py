from django import forms
from core.models import *


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'sex', 'age', 'academy', 'department', 'location', 'major')