from django.contrib import admin
from app_models.models import Issue, PullRequest, User, Repository, Label

admin.site.register(Issue)
admin.site.register(PullRequest)
admin.site.register(User)
admin.site.register(Repository)
admin.site.register(Label)
