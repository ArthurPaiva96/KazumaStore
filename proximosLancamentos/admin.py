from django.contrib import admin

# Register your models here.
from proximosLancamentos.models import ProximoLancamento


class ProximoLancamentoAdmin(admin.ModelAdmin):
    list_display = ['nome','sinopse','imagem','nomeAbreviado','dataInicioFinal','temporadaDeLancamento','diaHoraDeExibicao',
                    'produtores','licenciadores','estudio','midiaOriginal','generos']
    search_fields = ['nome','produtores','estudio','generos','temporadaDeLancamento']

admin.site.register(ProximoLancamento,ProximoLancamentoAdmin)