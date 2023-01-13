from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

from . import views
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('auth/', include('user_auth.urls')),
    path('issues/', views.issues, name="issues"),
    path('pulls/', views.pulls, name="pulls"),
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('profile/', views.profile, name="profile"),
    path('editprofile/', views.edit_profile, name="edit_profile"),
    path('projects/', views.projects, name="projects"),
    path('newproject/', views.newproject, name="newproject"),
    path('add_issue_to_project/', views.add_issue_to_project, name="add_issue_to_project")  
]
