from django.db import models
from datetime import datetime
from pessoas.models import Pessoa

class Receita(models.Model):
    nome_receita = models.CharField(max_length=100)
    ingrediente = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    date_receita = models.DateTimeField(default=datetime.now, blank=True)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    foto = models.ImageField('fotos/%d/%m/%Y/', blank= True)
    publicado = models.BooleanField(default=False)