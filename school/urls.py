from django.urls import path
from . import views

urlpatterns = [
    path('department' , views.department , name="department"),
    path('delete-department/<int:id>', views.delete_department , name="delete-department"),

    path('section' , views.section , name="section"),
    path('delete-section/<int:id>', views.delete_section , name="delete-section"),

    path('teacher' , views.teacher , name="teacher"),
    path('delete-teacher/<int:id>', views.delete_teacher, name="delete-teacher"),
    path('update-teacher/<int:pk>', views.UpdateTeacher.as_view(), name="update-teacher"),

    path('student', views.student.as_view(), name="student"),
    path('update-student/<int:pk>', views.UpdateStudent.as_view(), name="update-student"),
    path('delete-student/<int:id>', views.delete_student, name="delete-student"),

    path('class', views.manage_class.as_view(), name="class"),
    path('update-class/<int:pk>', views.UpdateClass.as_view(), name="update-class"),
    path('delete-class/<int:id>', views.delete_class, name="delete-class"),
    
    path('course', views.course.as_view(), name="course"),
    path('update-course/<int:pk>', views.UpdateCourse.as_view(), name="update-course"),
    path('delete-course/<int:id>', views.delete_course, name="delete-course"),
]