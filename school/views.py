from django.shortcuts import render ,redirect
from .models import Department, Section , Teacher , Student , Class , Course
from django.views.generic.edit import UpdateView , CreateView

from .forms import DepartmentForm , SectionForm , TeacherForm , StudentForm , ClassForm , CourseForm

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


class UpdateTeacher( UpdateView):

    def test_func(self):
        login_url  = 'login/'
        return(self.request.user)
    
    model = Teacher

    fields = ('__all__')

class student(CreateView):
    def test_func(self):
        login_url = 'login/'
        return(self.request.user)

    
    def get(self,request):
        
        std_form = StudentForm()
        students = Student.objects.all()
        context = {
            'students': students,
            'std_form' :std_form,
        }
        return render(request, 'school/student.html', context)
    
    def post(self, request):
        std_form = StudentForm(request.POST , request.FILES)
        context = {
            'std_form' : StudentForm,
        }

        if std_form.is_valid():
            std_form.save()
            return redirect('school:student')
        else:
            print(StudentForm.errors)
            return render(request, 'school/student.html', context)
  
        
        return redirect('school:student')

def delete_student(request , id):
    Student.objects.get(id=id).delete()
    render(request , 'school/teacher.html' , {'response' : "Student deleted successfully"})
    return redirect('school:teacher')

class UpdateStudent( UpdateView):

    def test_func(self):
        login_url  = 'login/'
        return(self.request.user)
    
    model = Student

    fields = ('__all__')


class manage_class(CreateView):
    def test_func(self):
        login_url = 'login/'
        return(self.request.user)

    
    def get(self,request):
        
        class_form = ClassForm()
        classes = Class.objects.all()
        context = {
            'classes': classes,
            'class_form' : class_form,
        }
        return render(request, 'school/class.html', context)
    
    def post(self, request):
        class_form = ClassForm(request.POST , request.FILES)
        context = {
            'class_form' : ClassForm,
        }

        if class_form.is_valid():
            c = class_form.save(commit=False)
            c.save()
            return redirect('school:class')
        else:
            print(ClassForm.errors)
            return render(request, 'school/class.html', context)
  
        
        return redirect('school:class')

class UpdateClass( UpdateView):

    def test_func(self):
        login_url  = 'login/'
        return(self.request.user)
    
    model = Class

    fields = ('__all__')

def delete_class(request , id):
    Class.objects.get(id=id).delete()
    render(request , 'school/class.html' , {'response' : "Teacher deleted successfully"})
    return redirect('school:class')

class course(CreateView):
    def test_func(self):
        login_url = 'login/'
        return(self.request.user)

    
    def get(self,request):
        
        course_form = CourseForm()
        courses = Course.objects.all()
        context = {
            'courses': courses,
            'course_form' : course_form,
        }
        return render(request, 'school/course.html', context)
    
    def post(self, request):
        course_form = CourseForm(request.POST , request.FILES)
        context = {
            'class_form' : course_form,
        }

        if course_form.is_valid():
            c = course_form.save(commit=False)
            c.save()
            return redirect('school:course')
        else:
            return render(request, 'school/course.html', context)
  
        
        return redirect('school:course')

class UpdateCourse( UpdateView):

    def test_func(self):
        login_url  = 'login/'
        return(self.request.user)
    
    model = Course

    fields = ('__all__')
    
def delete_course(request , id):
    Course.objects.get(id=id).delete()
    render(request , 'school/course.html' , {'response' : "Course deleted successfully"})
    return redirect('school:course')

