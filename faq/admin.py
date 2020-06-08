from django.contrib import admin

# Register your models here.
from faq.models import PerguntaERespostaHTML


class PerguntaERespostaHTMLAdmin(admin.ModelAdmin):
    list_display = ['htmlPergunta', 'htmlResposta']
    search_fields = ['htmlPergunta']

admin.site.register(PerguntaERespostaHTML, PerguntaERespostaHTMLAdmin)

