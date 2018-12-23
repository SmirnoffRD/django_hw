from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from authapp.forms import CustomUser_LoginForm, CustomUser_RegistrationForm
from django.contrib import auth
# Create your views here.

def login_view(request):
    title = 'Вход'

    login_form = CustomUser_LoginForm(data=request.POST or None)
    if request.method == 'POST' or login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main'))
    
    content = {'title': title, 'login_form': login_form}
    return render(request, 'authapp/login.html', content)

def registration_view(request):
    title = 'Регистрация'

    register_form = CustomUser_RegistrationForm()

    if request.method == 'POST':
        register_form = CustomUser_RegistrationForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('authapp:login'))
    else:
        register_form = CustomUser_RegistrationForm()
    
    content = {'title': title, 'register_form': register_form}
    return render(request, 'authapp/register.html', content)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('mainapp:main'))
