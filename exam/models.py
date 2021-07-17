from django.db import models
from school.models import Class , Student, Course
from django.urls import  reverse
# Create your models here.
class Exam(models.Model):
    grade = models.ForeignKey(Class , on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    result_date = models.DateField()
    published = models.BooleanField(default=False)
    exam_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)
    
    def get_absolute_url(self):
        return reverse('exam:exam')
    
    
class Result(models.Model):
    status_list = [
        ('Enabled', 'Enabled'),
        ('Disabled' , 'Disabled'),
        ('Pending', 'Pending')
    ]
    grade = models.ForeignKey(Class , on_delete=models.CASCADE)
    student = models.ForeignKey(Student , on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam , on_delete=models.CASCADE)
    percentage = models.FloatField(null=True, blank=True)
    GPA = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=15, choices=status_list)
    
    def __str__(self):
        return str(self.exam.name + self.exam.name)
    
class Mark(models.Model):
    result = models.ForeignKey(Result, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    marks = models.FloatField()



