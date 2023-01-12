from django.shortcuts import render
from app_models.issue import Issue
from app_models.pull_request import PullRequest
from app_models.label import Label
from app_models.enums import IssueStatus
from app_models.enums import PullRequestStatus

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
