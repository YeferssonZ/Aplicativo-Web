from django.urls import path
from . import views
from .views import CustomLoginView, CustomSignupView

app_name = 'emulator'

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('accounts/login/', CustomLoginView.as_view(), name='account_login'),
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
    path('logout/', views.logout_view, name='logout'),
]
