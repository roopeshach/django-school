from django.db import models
from django.urls import  reverse
# Create your models here.
class school_info(models.Model):
    name = models.CharField(max_length=254)
    address = models.CharField( max_length=254)
    phone = models.CharField(max_length=14)
    email = models.CharField(max_length=254)
    
    def __str__(self):
        return self.name


class Admin(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=150)
    username = models.CharField(max_length=50)
    password = models.CharField( max_length=250)

    def __str__(self):
        return self.name

class Session(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Section(models.Model):
    name = models.CharField(max_length=100)
    room_no = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

class Course(models.Model):
    name = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course_type = models.CharField(max_length=100)
    course_time = models.CharField(max_length=254)

    def __str__(self):
        return str(self.name + self.department.name)

class Teacher(models.Model):
    genders = [
        ('Male', 'Male'),
        ('Female' , 'Female'),
        ('Others', 'Others')
    ]
    name = models.CharField(max_length=254)
    department = models.ForeignKey(Department , on_delete=models.CASCADE)
    email = models.CharField(max_length=254 , default=None)
    address = models.CharField(max_length=254 )
    phone = models.CharField(max_length=254)
    gender = models.CharField(max_length=10, choices=genders)
    salary = models.FloatField()
    image = models.ImageField(null=True , upload_to='teachers/')
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('school:teacher')



class Class(models.Model):
    name = models.CharField(max_length=254)
    class_teacher = models.ForeignKey(Teacher , on_delete=models.CASCADE)
    is_active = models.IntegerField()
    def __str__(self):
        return str(self.name)


class Student(models.Model):
    sid = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    address = models.CharField(max_length=254)
    caste = models.CharField(max_length=254)
    gender = models.CharField(max_length=10)
    dob = models.DateTimeField(auto_now_add=False)
    father_name = models.CharField(max_length=254)
    mother_name = models.CharField(max_length=254)
    contact = models.CharField(max_length=254)
    grade = models.ForeignKey(Class , on_delete=models.CASCADE)
    section = models.ForeignKey(Section , on_delete=models.CASCADE)
    
    image = models.ImageField(null=True , upload_to='students/')

