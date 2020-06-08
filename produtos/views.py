import numpy
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.core.paginator import Paginator
# Create your views here.
from produtos.models import Produto, Carrinho
from produtos.forms import CadastrarProdutoForm

@login_required
def index(request):
    return render(request, 'produtos.html', {"produtos" : Produto.objects.all()})

@login_required
def comprar(request, produtoId):
    carrinhoDoUsuarioLogado = getCarrinhoPerfilLogado(request)
    carrinhoDoUsuarioLogado.comprar(produtoId,int(request.POST['quantidade']))
    return render(request, 'carrinho.html', retornaDadosCarrinho(request))

@login_required
def carrinho(request):
    return render(request, 'carrinho.html', retornaDadosCarrinho(request))

@login_required
def alterarQuantidadeAjax(request):
    produtoId = int(request.POST['produtoId'])
    quantidade = int(request.POST['quantidade'])
    getCarrinhoPerfilLogado(request).alterarQuantidade(produtoId,quantidade)
    return render(request, 'carrinho.html', retornaDadosCarrinho(request))

@login_required
def deletarProdutoDoCarrinhoAjax(request):
    produtoId = int(request.POST['produtoId'])
    getCarrinhoPerfilLogado(request).deletarProduto(produtoId)
    return render(request, 'carrinho.html', retornaDadosCarrinho(request))

def retornaDadosCarrinho(request):
    carrinhoDoUsuarioLogado = getCarrinhoPerfilLogado(request)
    todosOsItensDoCarrinho = carrinhoDoUsuarioLogado.retornaTodosItensDoCarrinho()
    precoTotalDosItensDoCarrinho = calculaPrecoTotalDosItensDoCarrinho(todosOsItensDoCarrinho)
    return {"itensCarrinho": zip(todosOsItensDoCarrinho, precoTotalDosItensDoCarrinho),
                                                "precoTotalCarrinho":numpy.sum(precoTotalDosItensDoCarrinho)}

def calculaPrecoTotalDosItensDoCarrinho(itens):
    precosTotais = []
    for item in itens:
        precosTotais.append(item.quantidade*item.produto.preco)
    return precosTotais

@login_required
def getCarrinhoPerfilLogado(request):
    try:
        carrinhoUsuarioLogado = Carrinho.objects.get(usuario=request.user)

    except Carrinho.DoesNotExist:
        carrinhoUsuarioLogado = Carrinho(request.user.id)
        carrinhoUsuarioLogado.save()
    return carrinhoUsuarioLogado

def buscar(request):
    todosOsProdutosBuscaAlterar = Produto.objects.all()
    todosOsProdutosBuscaExcluir = Produto.objects.all()

    if 'buscaAlterar' in request.GET:
        nomeBuscado = request.GET['buscaAlterar']

        if buscar:
            todosOsProdutosBuscaAlterar = todosOsProdutosBuscaAlterar.filter(nome__icontains=nomeBuscado)
            return render(request, 'produtosAdministracaoBusca.html', {"produtosAlterar": todosOsProdutosBuscaAlterar,
                                                                       "produtosExcluir": todosOsProdutosBuscaExcluir,
                                                                       "collapse":['',' in show ','']})

    if 'buscaExcluir' in request.GET:
        nomeBuscado = request.GET['buscaExcluir']

        if buscar:
            todosOsProdutosBuscaExcluir = todosOsProdutosBuscaExcluir.filter(nome__icontains=nomeBuscado)
            return render(request, 'produtosAdministracaoBusca.html', {"produtosAlterar" : todosOsProdutosBuscaAlterar,
                                                                        "produtosExcluir" : todosOsProdutosBuscaExcluir,
                                                                        "collapse":['','',' in show ']})
def paginacao(request):
    produtos = Produto.objects.all()
    produtosPaginados = Paginator(produtos, 1)
    pagina = request.GET.get('pagina')
    produtos = produtosPaginados.get_page(pagina)
    return produtos;

def collapsePaginacao(request):
    collapse = [' in show ', '', '']
    if "formularioAlterarProduto" in str(request.GET.get('idTag')):
        collapse[1] = ' in show '
    elif "formularioExcluirProduto" in str(request.GET.get('idTag')):
        collapse[2] = ' in show '
    return collapse

class AdministradorProdutosCadastrar(View):

    template_name = 'produtosAdministracao.html'

    def get(self, request):
        collapse = collapsePaginacao(request)
        return render(request, self.template_name, {"produtos": paginacao(request), "collapse": collapse})

    def post(self, request):
        form = CadastrarProdutoForm(request.POST)

        if form.is_valid():

            novoProduto = Produto(nome= form.data['nome'], descricao= form.data['descricao'], preco= form.data['preco'],
                                  foto= form.data['foto'], classe= form.data['classe'])
            novoProduto.save()

            return redirect('')

        return render(request, self.template_name, { 'form': form, "produtos" : Produto.objects.all() })

class AdministradorProdutosAlterar(View):

    template_name = 'produtosAdministracao.html'

    def get(self, request):
        collapse = collapsePaginacao(request)
        return render(request, self.template_name, {"produtos": paginacao(request), "collapse": collapse})

    def post(self, request, pk):

        produtoAlterado = Produto.objects.get(pk=pk);
        form = CadastrarProdutoForm(request.POST, instance=produtoAlterado)

        if form.is_valid():

            form.save();

            return redirect('')

        return render(request, self.template_name, { 'form': form,"produtos" : Produto.objects.all() })

class AdministradorProdutosDeletar(View):

    template_name = 'produtosAdministracao.html'

    def get(self, request):
        collapse = collapsePaginacao(request)
        return render(request, self.template_name, {"produtos": paginacao(request), "collapse": collapse})

    def post(self, request, pk):

        produtoDeletado = Produto.objects.get(pk=pk);
        produtoDeletado.delete()

        return redirect('')
