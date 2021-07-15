from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index , name="index"),
    path('school-info', views.school_info, name="school-info"),
    
]