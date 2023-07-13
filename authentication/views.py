from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import User
from . import forms


def sign_up_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            # Redirigez vers la page appropriée en fonction du rôle de l'utilisateur
            if user.role == 'ADMIN':
                return redirect('/admin')
            elif user.role == 'USER':
                return redirect('user_page')
            elif user.role == 'SUPPLIER':
                return redirect('supplier_page')
            
    return render(request, 'authentication/sign_up.html', context={'form': form})

def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                if user.role == User.USER:  # check if user is a regular user
                    return redirect('user_page')  # change to your user page
                elif user.role == User.SUPPLIER:  # check if user is a supplier
                    return redirect('supplier_page')  # change to your supplier page
                else:
                    return redirect('/admin')  # change to your admin page
            else:
                message = 'Identifiants invalides.'
    return render(
        request, 'authentication/login.html', context={'form': form, 'message': message})

@login_required
def user_home(request):
    return render(request, 'authentication/user_home.html')

@login_required
def supplier_page(request):
    return render(request, 'authentication/supplier_page.html')

