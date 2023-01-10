from django.shortcuts import render
from app_models.issue import Issue, Label

from user_auth.forms import SignInForm
from django.contrib.contenttypes.models import ContentType



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

def issues(request):
    user = request.user

    issues = Issue.objects.filter(creator__id=user.id).all()

    for issue in issues:
        content_type = ContentType.objects.get_for_model(Label)
        model_class = content_type.model_class()

        # Use the model class to filter the objects
        labels = model_class.objects.filter(pk=issue.id).all()
        issue.labels = labels


    return render(request, 'issues.html', {'user': user, 'issues': issues})
