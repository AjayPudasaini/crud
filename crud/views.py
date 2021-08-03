from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student
from django.contrib import messages


def home(request):
    s = Student.objects.all()
    if request.method == "POST":
        data = request.POST
        Iemail = data['email']
        Iusername = data['username']
        Iaddress = data['address']

        a = Student.objects.create(username=Iusername, email=Iemail, address=Iaddress)
        if a:
            messages.success(request, 'data was created')
            return redirect('/')
        else:
            messages.warning(request, 'failed')
    contex = {'student':s}
    return render(request, 'crud/home.html', contex)



def detail(request, myId):
    s = Student.objects.get(id=myId)
    contex = {'student':s}
    return render(request, 'crud/detail.html', contex)


def delete(request, id):
    s = Student.objects.get(id=id)
    if request.method == "POST":
        s.delete()
        messages.success(request, 'data deleted')
        return redirect('/')



def update(request, id):
    s = Student.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        s.email = data['email']
        s.username = data['username']
        s.address = data['address']
        s.save()
        if s:
            messages.success(request, 'data was updated')
            return redirect('/')
        else:
            messages.warning(request, 'failed')
    contex = {'student':s}
    return render(request, 'crud/update.html', contex)


def about(request):
    return render(request, 'about.html')



def contact(request):
    return render(request, 'contact.html')

