from django.urls import path

from clientes.views import clienteList, ClienteView, ClienteInsert, ClienteEdit, ClienteDelete

urlpatterns = [
    path('', clienteList, name='ClientesList'),
    path('view/<int:pk>', ClienteView, name='ClienteView'),
    path('insert', ClienteInsert, name='ClienteInsert'),
    path('edit/<int:pk>', ClienteEdit, name='ClienteEdit'),
    path('delete/<int:pk>', ClienteDelete, name='ClienteDelete'),
]
