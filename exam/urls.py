from django.urls import  path
from . import views

urlpatterns =[
    path('exam' , views.manage_exam.as_view() , name="exam"),
    path('delete-exam/<int:id>', views.delete_exam, name="delete-exam"),
    path('update-exam/<int:pk>', views.UpdateExam.as_view(), name="update-exam"),
]