from django.db import models
from .Classes import ClassList

class Passagem(models.Model):
    origem = models.CharField(max_length= 100)
    destino = models.CharField(max_length=100)
    ida = models.DateField()
    volta = models.DateField()
    data_pesquisa = models.DateField()
    informacoes = models.TextField(max_length=200, blank=True)
    classe = models.CharField(max_length=4, choices=ClassList.choices)

