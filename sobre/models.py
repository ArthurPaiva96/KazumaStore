from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Quote(models.Model):

    texto = models.CharField(max_length=255, null=False)
    estilo = models.CharField(max_length=255,null=True, blank=True)
    classe = models.CharField(max_length=255, null=False)