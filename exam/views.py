from django.shortcuts import render , redirect
from django.views.generic.edit import UpdateView , CreateView
 
# Create your views here.
from .models import Exam
from .forms import ExamForm

class manage_exam(CreateView):
    def test_func(self):
        login_url = 'login/'
        return(self.request.user)

    
    def get(self,request):
        
        exam_form = ExamForm()
        exams = Exam.objects.all()
        context = {
            'exams': exams,
            'exam_form' : exam_form,
        }
        return render(request, 'exam/exam.html', context)
    
    def post(self, request):
        exam_form = ExamForm(request.POST , request.FILES)
        context = {
            'class_form' : exam_form,
        }

        if exam_form.is_valid():
            c = exam_form.save(commit=False)
            c.save()
            return redirect('exam:exam')
        else:
            return render(request, 'exam/exam.html', context)
        
        return redirect('exam:exam')

class UpdateExam( UpdateView):

    def test_func(self):
        login_url  = 'login/'
        return(self.request.user)
    
    model = Exam

    fields = ('__all__')
    
def delete_exam(request , id):
    Exam.objects.get(id=id).delete()
    render(request , 'exam/exam.html' , {'response' : "exam deleted successfully"})
    return redirect('exam:exam')