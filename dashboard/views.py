from django.shortcuts import render , redirect
from school.models import  school_info as SI , Teacher , Course
from school.forms import SchoolForm , TeacherForm
# Create your views here.
def index(request):
    return render(request , 'dashboard/index.html' )


def school_info(request):
    if request.method == "POST":  
        info = SchoolForm(request.POST)
        context = { 
            'response' : "School details added successfully"
        }
        if info.is_valid():
            info.save()
            return render(request, 'dashboard/school-details.html' ,context)

    detail = SI.objects.order_by('-id')[0]
    context ={
        'detail' : detail,
    }
    return render(request , 'dashboard/school-details.html' , context)

def class_course(request , id):

    courses = Course.objects.all().filter(grade=id)

    context = {
         'courses' :courses,
     }

    return render(request, 'dashboard/class_course.html' , context)