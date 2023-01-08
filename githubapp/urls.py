from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

from . import views
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('auth/', include('user_auth.urls')),
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
]
