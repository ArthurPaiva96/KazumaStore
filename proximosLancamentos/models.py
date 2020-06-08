from django.db import models

# Create your models here.
class ProximoLancamento(models.Model):
    nome = models.CharField(max_length=500, null=False)
    sinopse = models.CharField(max_length=500, null=False)
    imagem = models.CharField(max_length=500, null=False)
    nomeAbreviado = models.CharField(max_length=100, null=False)
    dataInicioFinal = models.CharField(max_length=500, null=False)
    temporadaDeLancamento = models.CharField(max_length=100, null=False)
    diaHoraDeExibicao = models.CharField(max_length=100, null=False)
    produtores = models.CharField(max_length=500, null=False)
    licenciadores = models.CharField(max_length=500, null=False)
    estudio = models.CharField(max_length=500, null=False)
    midiaOriginal = models.CharField(max_length=500, null=False)
    generos = models.CharField(max_length=500, null=False)