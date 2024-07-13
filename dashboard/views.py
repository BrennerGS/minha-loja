from django.http import HttpResponsePermanentRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages

from clientes.models import Clientes

# Create your views here.
def clienteList(request):
    try:
        ClientesFor = Clientes.objects.all()
        return render(request, 'Clientes.html', {'Clientes': ClientesFor})
    except Exception as e:
        messages.warning(request, "Erro ao carregar dados por favor tente novamente mais tarde!")
        return HttpResponsePermanentRedirect(reverse('ClientesList'))
    