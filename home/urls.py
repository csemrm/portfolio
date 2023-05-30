from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),

    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),
]
