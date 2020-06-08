from django.db import models

# Create your models here.
class PerguntaERespostaHTML(models.Model):
    htmlPergunta = models.CharField(max_length=9999,null=False)
    htmlResposta = models.CharField(max_length=9999,null=False)