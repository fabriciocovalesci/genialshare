from django.shortcuts import render
from core.artigo.models import Artigo

def home(request):
    post = Artigo.objects.all()
    return render(request, 'home.html')




def artigos(request):
    posts =  Artigo.objects.all()
    return render(request, 'principal.html' ,{'posts' : posts})

def post(request, post_id):
    post =  Artigo.objects.get(pk=post_id)
    return render(request,'post.html',  {'post' : post})

def tutoriais(request):
    return render(request, 'tutoriais.html')


def about(request):
    return render(request, 'about.html')


def contato(request):
    return render(request, 'contato.html')

