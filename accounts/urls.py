# accounts/urls.py

from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('admin-area/', admin_view, name='admin_area'),
    path('admin-only/', admin_view, name='admin_view'),
    path('editor-only/', editor_view, name='editor_view'),
    path('viewer-only/', viewer_view, name='viewer_view'),
]
