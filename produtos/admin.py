from django.contrib import admin

# Register your models here.
from produtos.models import Produto, Carrinho


class ProdutoAdmin(admin.ModelAdmin):

    list_display = ['nome', 'descricao', 'preco', 'foto', 'classe']
    search_fields = ['nome']

admin.site.register(Produto, ProdutoAdmin)

class CarrinhoAdmin(admin.ModelAdmin):

    list_display = ['usuario']
    search_fields = ['usuario']

admin.site.register(Carrinho, CarrinhoAdmin)