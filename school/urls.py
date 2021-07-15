from django.urls import path
from . import views

urlpatterns = [
    path('department' , views.department , name="department"),
    path('delete-department/<int:id>', views.delete_department , name="delete-department"),
    path('section' , views.section , name="section"),
    path('delete-section/<int:id>', views.delete_section , name="delete-section"),
    path('teacher' , views.teacher , name="teacher"),
    path('delete-teacher/<int:id>', views.delete_teacher, name="delete-teacher"),
    path('update-teacher/<int:id>', views.update_teacher, name="delete-teacher")
]