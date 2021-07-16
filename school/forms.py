from django import forms
from .models import school_info , Admin , Teacher , Department , Section , Student , Class , Course
class SchoolForm(forms.ModelForm):
    class Meta:
        model = school_info
        fields = '__all__'

class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = '__all__'

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'

class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = '__all__'

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = '__all__'

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'