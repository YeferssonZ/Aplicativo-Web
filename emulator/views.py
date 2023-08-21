from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.signals import user_logged_in
from allauth.account.views import LoginView, SignupView

# Create your views here.


def index(request):
    return render(request, 'contenido.html')

@login_required
def profile(request):
    # Obtener la información del usuario autenticado
    user = request.user
    # Puedes agregar más detalles según tus necesidades, como el nombre, la dirección, etc.

    return render(request, 'profile.html', {'user': user})

def logout_view(request):
    logout(request)
    return redirect('emulator:index')

class CustomLoginView(LoginView):
    template_name = 'socialaccount/login.html'

class CustomSignupView(SignupView):
    template_name = 'socialaccount/signup.html'