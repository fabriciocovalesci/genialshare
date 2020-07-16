from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('artigos/', views.artigos, name='artigos'),
    path('tutoriais/', views.tutoriais, name='tutoriais'),
    path('about/', views.about, name='about'),
    path('contato/', views.contato, name='contato'),
]