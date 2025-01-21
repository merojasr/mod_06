# users/views.py
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from . forms import CustomUserCreationForm
from django.contrib.auth.models import Permission

# Vista para el login
class CustomLoginView(LoginView):
    template_name = "auth/login.html"
    redirect_authenticated_user = True
    
# Vista para el logout
class CustomLogoutView(LogoutView):
    template_name = "auth/logout.html"
    next_page = '/'

# Vista para el registrofrom django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            permiso = Permission.objects.get(codename="visualizar_catalogo")
            user.user_permissions.add(permiso)
            login(request, user)  
            return redirect('index')  
    else:
        form = CustomUserCreationForm()

    return render(request, "auth/register.html", {"form": form})