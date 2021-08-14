from django.shortcuts import render, redirect
from .forms import  UserRegister
from django.contrib import messages



def account(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'user created')
            return  redirect('login')
    else:
        form = UserRegister()

    contex = {'form':form}
    return render(request, 'users/account.html', contex)
