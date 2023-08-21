from django.urls import path
from . import views

app_name = 'emulator'

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('signup/', views.CustomSignupView.as_view(), name='signup'),
    path('logout/', views.logout_view, name='logout'),

]