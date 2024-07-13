from django.urls import path

from clientes.views import clienteList

urlpatterns = [
    path('', clienteList, name='ClientesList'),
]
