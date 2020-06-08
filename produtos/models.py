from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Produto(models.Model):

    nome = models.CharField(max_length=99999, null=False)
    descricao = models.CharField(max_length=99999, null=False)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    foto = models.CharField(max_length=99999)
    classe = models.CharField(max_length=99999)

class Carrinho(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def comprar(self,produtoId,quantidade):
        produtoComprado = Produto.objects.get(id=produtoId)

        try:
            itemCarrinho = ItemCarrinho.objects.get(carrinho=self,produto=produtoComprado)
            itemCarrinho.quantidade +=quantidade
            itemCarrinho.save()
        except ItemCarrinho.DoesNotExist:
            ItemCarrinho(produto=Produto.objects.get(id=produtoId),quantidade=quantidade,carrinho=self).save()

    def alterarQuantidade(self,produtoId,quantidade):
        produtoComprado = Produto.objects.get(id=produtoId)
        itemCarrinho = ItemCarrinho.objects.get(carrinho=self, produto=produtoComprado)
        itemCarrinho.quantidade = quantidade
        itemCarrinho.save()

    def deletarProduto(self,produtoId):
        produtoComprado = Produto.objects.get(id=produtoId)
        itemCarrinho = ItemCarrinho.objects.get(carrinho=self, produto=produtoComprado)
        itemCarrinho.delete()

    def retornaTodosItensDoCarrinho(self):
        return ItemCarrinho.objects.filter(carrinho_id=self.id)

class ItemCarrinho(models.Model):
    produto = models.ForeignKey('Produto', on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=0)
    carrinho = models.ForeignKey(Carrinho, related_name='itensCarrinho', on_delete=models.CASCADE)