from django.urls import path
from . import views

app_name = 'emulator'

urlpatterns = [
    path('', views.index, name='index'),

]