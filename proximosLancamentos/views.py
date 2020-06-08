from django.shortcuts import render

# Create your views here.
from proximosLancamentos.models import ProximoLancamento


def exibePaginaProximosLancamentos(request):
    return render(request,'proximosLancamentos.html',{'proximosLancamentos' : ProximoLancamento.objects.all()})