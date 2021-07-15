from django.shortcuts import redirect, render
# Create your views here.
from school.forms import AdminForm
from school.models import Admin


def register(request):
    if request.method == "POST":
        uname = request.POST['username']
        query = Admin.objects.all().get(username=uname)
        print(query)
        if query:
            render(request  , 'auth/register.html' , {'error' : 'Username not available'})
        else:
            admin = AdminForm(request.POST)
            if admin.is_valid():
                admin.save()
            
            

    return render(request  , 'auth/register.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        admin = Admin.objects.all().get(username=username)
        if admin.username == request.POST['username'] and admin.password == request.POST['password']:
            return redirect('dashboard:index')

    return render(request , 'auth/login.html')
