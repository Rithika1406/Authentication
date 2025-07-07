from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from . forms import RegistrationForm
from .utils import is_in_group
# Create your views here.

#Register API
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html',{'form':form})


#Login API
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'registration/login.html',{'error':'Invalid Credentials'})
    return render(request, 'registration/login.html')

@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')

@login_required
@user_passes_test(lambda u: u.is_staff)
def admin_view(request):
    return render(request, 'admin_only.html')


@login_required
@user_passes_test(lambda u: is_in_group(u, 'Admin'))
def admin_view(request):
    return render(request, 'roles/admin.html')

@login_required
@user_passes_test(lambda u: is_in_group(u, 'Editor'))
def editor_view(request):
    return render(request, 'roles/editor.html')

@login_required
@user_passes_test(lambda u: is_in_group(u, 'Viewer'))
def viewer_view(request):
    return render(request, 'roles/viewer.html')
