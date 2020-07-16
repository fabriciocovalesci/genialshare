from django.shortcuts import render
from core.artigo.models import Artigo

def home(request):
    post = Artigo.objects.all()
    return render(request, 'base.html', {'post' : post})


def artigos(request):
    return render(request, 'artigos.html')


def tutoriais(request):
    return render(request, 'tutoriais.html')


def about(request):
    return render(request, 'about.html')


def contato(request):
    return render(request, 'contato.html')

