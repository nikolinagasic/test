from django.shortcuts import render
from django.shortcuts import redirect

from app_models.issue import Issue
from app_models.pull_request import PullRequest
from app_models.label import Label
from app_models.enums import IssueStatus
from app_models.enums import PullRequestStatus
from user_auth.forms import SignInForm
from .forms import UserForm
from app_models.models import User


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

def profile(request):
    print(request)
    if request.user.is_authenticated:
        # Get the currently logged-in user
        if request.method == "POST":
            user = User.objects.get(id=request.user.id)
            user.delete()            
            return redirect('logout')
        else:
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
    
     
def issues(request):
    user = request.user
    issues = Issue.objects.filter(creator__id=user.id).all()
    opened_issues = list(filter(lambda issue: issue.state == IssueStatus.OPENED, issues))
    closed_issues = list(filter(lambda issue: issue.state == IssueStatus.CLOSED, issues))

    # Get labels for each issue
    for issue in issues:
        content_type = ContentType.objects.get_for_model(Label)
        model_class = content_type.model_class()

        labels = model_class.objects.filter(pk=issue.id).all()
        issue.labels = labels

    return render(request, 'issues.html', {'user': user, 'opened_issues': opened_issues, "opened_issues_num": len(opened_issues), "closed_issues": closed_issues, "closed_issues_num": len(closed_issues)})

def pulls(request):
    user = request.user
    pulls = PullRequest.objects.filter(creator__id=user.id).all()
    opened_pulls = list(filter(lambda pull: pull.state == PullRequestStatus.OPENED, pulls))
    closed_pulls = list(filter(lambda pull: pull.state == PullRequestStatus.CLOSED, pulls))

    # Get labels for each pull request
    for pull in pulls:
        content_type = ContentType.objects.get_for_model(Label)
        model_class = content_type.model_class()

        labels = model_class.objects.filter(pk=pull.id).all()
        pull.labels = labels

    return render(request, 'pull_requests.html', {'user': user, 'opened_pulls': opened_pulls, "opened_pulls_num": len(opened_pulls), "closed_pulls": closed_pulls, "closed_pulls_num": len(closed_pulls)})      

def projects(request):
    return render(request, 'projects.html')

def newproject(request):
    states = [IssueStatus.OPENED, IssueStatus.CLOSED]
    issues = Issue.objects.filter(creator__id=request.user.id).all()
    issues = [{"title":"Some title", "repository":"Some user", "state":states[0], "creator":request.user}, {"title":"Some other title", "repository":"Some other user", "state":states[0], "creator":request.user}]
    return render(request, 'newproject.html', {'user':request.user, 'states': states, 'issues':issues})

def add_issue_to_project(request):  
    if request.user.is_authenticated:
        states = [IssueStatus.OPENED, IssueStatus.CLOSED]
        issues = [{"title":"Some title", "repository":"Some user", "state":states[0], "creator":request.user}, {"title":"Some other title", "repository":"Some other user", "state":states[0], "creator":request.user}]
        if request.method == 'POST':
            title = form.cleaned_data['title']
            repository = form.cleaned_data['assigned']
            state = form.cleaned_data['state']
            issue = Issue.objects.create(title=title,repository=repository, state=state, creator=request.user)
            return redirect('newproject',{'user':request.user, 'states': states, 'issues':issues})
        else:
            return render(request, 'add_issue_to_project.html', {'states': states, 'issues':issues})
    else:
        # Render template for log in
        form = SignInForm()
        return render(request, 'sign_in.html', {'form': form})
