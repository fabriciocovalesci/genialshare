from django.shortcuts import render, get_object_or_404, redirect, HttpResponse, HttpResponseRedirect, resolve_url
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic.edit import UpdateView
from django.views.generic import TemplateView
from django.http import JsonResponse



def home(request):
    return render(request, 'index.html')

    
class Login(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'