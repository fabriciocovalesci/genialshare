from django.db import models
from django.contrib.auth.models import User 
from django.conf import settings
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField



class Artigo(models.Model):
    titulo = models.CharField(max_length=255)
    resumo = RichTextField()
    conteudo = RichTextUploadingField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(default=timezone.now)

        
    class Meta:
        verbose_name = "Artigo"
        verbose_name_plural = "Artigos"

