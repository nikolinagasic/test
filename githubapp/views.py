from django.shortcuts import render
from django.shortcuts import redirect

from user_auth.forms import SignInForm
from .forms import UserForm
from app_models.models import User



def index(request):

    if request.user.is_authenticated:
        # Get the currently logged-in user
        user = request.user
        # Render a template with the user information
        return render(request, 'index.html', {'user': user})
    else:
        # Render template for log in
        form = SignInForm()
        return render(request, 'sign_in.html', {'form': form})

def profile(request):

    if request.user.is_authenticated:
        # Get the currently logged-in user
        user = request.user
        # Render a template with the user information
        profile = User.objects.filter(username=user.username)[0]
        return render(request, 'profile.html', {'user': user, 'profile': profile})
    else:
        # Render template for log in
        form = SignInForm()
        return render(request, 'sign_in.html', {'form': form})
 
def edit_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                firstName = form.cleaned_data['firstName']
                lastName = form.cleaned_data['lastName']
                bio = form.cleaned_data['bio']
                company = form.cleaned_data['company']
                website = form.cleaned_data['website']
                user = User.objects.update(username=request.user.username,firstName=firstName, lastName=lastName, bio=bio, company=company, website=website)
            return redirect('profile')
        else:
            form = UserForm()
            return render(request, 'edit_profile.html', {'form': form})
    else:
        # Render template for log in
        form = SignInForm()
        return render(request, 'sign_in.html', {'form': form})
    
     