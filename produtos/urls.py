"""kazumaStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from produtos.views import AdministradorProdutosCadastrar, AdministradorProdutosAlterar, AdministradorProdutosDeletar
import produtos
from produtos import views
urlpatterns = [
    path('', views.index, name=''),
    path('adm_produtos', AdministradorProdutosCadastrar.as_view(), name='admProdutosCadastrar'),
    path(r'^adm_produtos(?P<pk>[0-9]+)', AdministradorProdutosAlterar.as_view(), name='admProdutosAlterar'),
    path(r'^adm_produtos/deletar/(?P<pk>[0-9]+)', AdministradorProdutosDeletar.as_view(), name='admProdutosDeletar'),
    path('adm_produtos/busca', views.buscar, name='buscar'),
    path(r'^comprar/(?P<produtoId>[0-9]+)', views.comprar, name='comprar'),
    path('carrinho', views.carrinho, name='carrinho'),
    path('carrinho/alterarQuantidadeAjax/', views.alterarQuantidadeAjax, name='alterarQuantidadeAjax'),
    path('carrinho/deletarProdutoAjax/', views.deletarProdutoDoCarrinhoAjax, name='deletarProdutoDoCarrinhoAjax')
]
