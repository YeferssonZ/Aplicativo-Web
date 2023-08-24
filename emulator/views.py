from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.signals import user_logged_in
from allauth.account.views import LoginView, SignupView


def index(request):
    return render(request, 'contenido.html')

@login_required
def profile(request):
    user = request.user

    return render(request, 'profile.html', {'user': user})

def logout_view(request):
    logout(request)
    return redirect('emulator:index')

# class CustomLoginView(LoginView):
#     template_name = 'socialaccount/login.html'
#     success_url = '/'  # Cambia esto a la ruta que desees después del inicio de sesión exitoso

# class CustomSignupView(SignupView):
#     template_name = 'socialaccount/signup.html'
#     success_url = '/'  # Cambia esto a la ruta que desees después del registro exitoso