from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, logout, authenticate


def user_register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {
        'form': form
    }
    return render(request, 'user/register.html', context)


def user_login(request):
    message = ''
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                message = 'Notugri usrname yoki parol kiritildi'

    context = {
        'form': form,
        'message': message
    }

    return render(request, 'user/login.html', context)


def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')
