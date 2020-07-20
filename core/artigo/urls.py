from django.urls import path, include
from core.artigo import urls
from . import views

urlpatterns = [
   
    path('', views.home, name='home'),
    path('artigos/', views.artigos, name='artigos'),
    path('tutoriais/', views.tutoriais, name='tutoriais'),
    path('about/', views.about, name='about'),
    path('contato/', views.contato, name='contato'),
]