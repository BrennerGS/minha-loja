from django.db import models
# Create your models here.

class Clientes(models.Model):
    Nome = models.CharField(max_length=100)
    CNPJ_CPF = models.CharField(unique=True, max_length=11)
    Email = models.CharField(max_length=100, unique=True)
    Celular = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.Nome} {self.CNPJ_CPF} {self.Email} {self.Celular}"
