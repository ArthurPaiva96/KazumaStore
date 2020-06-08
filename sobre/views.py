from django.shortcuts import render

# Create your views here.
from sobre.models import Quote


def exibePaginaSobre(request):
    return render(request, 'sobre.html',{'quotes':Quote.objects.all()})