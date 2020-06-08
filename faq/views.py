from django.shortcuts import render

# Create your views here.
from faq.models import PerguntaERespostaHTML


def exibePaginaFAQ(request):
    return render(request,'faq.html',{'htmlPerguntasERespostas':PerguntaERespostaHTML.objects.all()})