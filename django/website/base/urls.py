from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('myself/', views.myself, name='myself'),
    path('projects/', views.projects, name='projects'),
]