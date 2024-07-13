from django.contrib import admin

from clientes.models import Clientes

# Register your models here.

class ClientesAdmin(admin.ModelAdmin):

    list_display = ("Nome", "CNPJ_CPF", "Email", "Celular")
    search_fields = ('Nome', 'CNPJ_CPF', 'Email', 'Celular')

admin.site.register(Clientes, ClientesAdmin)