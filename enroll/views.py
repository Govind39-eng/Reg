from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from . models import User
# Create your views here.
def add_show(request):
    if request.method =='POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            stu = User(name= nm, email = em, password = pw)
            stu.save()
            fm = StudentRegistration()
            # print(nm, " + ",em , " + ", pw)
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'addandshow.html', {'form':fm, 'stu':stud})

def delete_data(request, id):
    if request.method == 'POST':
        pk = User.objects.get(pk = id)
        pk.delete();
        return HttpResponseRedirect('/')

def update_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk = id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk = id)
        fm = StudentRegistration(instance=pi)
    return render(request, "updatestudent.html",{'form':fm})