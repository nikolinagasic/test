from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .forms import SignInForm, SignUpForm
from app_models.models import User


def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            # Check the credentials and log the user in
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                # Return an error message
                pass
    else:
        form = SignInForm()
    return render(request, 'sign_in.html', {'form': form})


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Create the user account
            user = User.objects.create_user(
                form.cleaned_data['username'],
                form.cleaned_data['email'],
                form.cleaned_data['password'],
            )
            user.save()

            return redirect('sign_in')
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})
