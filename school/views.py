from django.shortcuts import render ,redirect
from .models import Department, Section , Teacher , Student
from django.views.generic.edit import UpdateView

from .forms import DepartmentForm , SectionForm , TeacherForm , StudentForm

# Create your views here.

def department(request):
    departments = Department.objects.all()

    context = {
        'departments': departments,
    }
    if request.method == 'POST':
        department = DepartmentForm(request.POST)
        print(department)
        if department.is_valid():
            department.save()
            context = {
                'departments': departments,
                'response' : "Department Added successfully"
             }
            return render(request , 'school/department.html' , context)

    
    return render(request , 'school/department.html' , context)

def delete_department(request , id):
    Department.objects.get(id=id).delete()
    render(request , 'school/department.html' , {'response' : "Department deleted successfully"})
    return redirect('school:department')

def section(request):
    sections = Section.objects.all()

    context = {
        'sections': sections,
    }
    if request.method == 'POST':
        section = SectionForm(request.POST)
        print(section)
        if section.is_valid():
            section.save()
            context = {
                'sections': sections,
                'response' : "Section Added successfully"
             }
            return render(request , 'school/section.html' , context)

    
    return render(request , 'school/section.html' , context)

def delete_section(request , id):
    Section.objects.get(id=id).delete()
    render(request , 'school/section.html' , {'response' : "Section deleted successfully"})
    return redirect('school:section')

def teacher(request):
    teachers = Teacher.objects.all()
    department = Department.objects.all()
    context = {
        'teachers': teachers,
        'department':department,
    }
    if request.method == 'POST':
        teacher = TeacherForm(request.POST, request.FILES)
        print(teacher)
        if teacher.is_valid():
            teacher.save()
            context = {
                'teachers': teachers,
                'department':department,
                'response' : "Teacher Added successfully"
             }
            return render(request , 'school/teacher.html' , context)

    
    return render(request , 'school/teacher.html' , context)

def delete_teacher(request , id):
    Teacher.objects.get(id=id).delete()
    render(request , 'school/teacher.html' , {'response' : "Teacher deleted successfully"})
    return redirect('school:teacher')

def update_teacher(request, id):
    teacher = Teacher.objects.get(id=id)
    department = Department.objects.all()
    if request.method == 'POST':
        teacher_form = TeacherForm(request.POST, request.FILES)
        if teacher_form.is_valid():
            teacher_form.save()
            teacher.delete()
            return redirect('school:teacher')
    

    context = {
        'teacher' : teacher,
        'department': department,
        }

    return render(request , 'school/teacher_update.html' , context)