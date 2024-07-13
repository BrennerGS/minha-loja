import re
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponsePermanentRedirect
from django.urls import reverse
from classe.validador import validador, ApenasNumero
from clientes.forms import ClienteForm
from clientes.models import Clientes
from django.contrib import messages
from logging import CRITICAL, ERROR, WARNING, INFO, DEBUG
from logging import basicConfig
from logging import critical, error, warning, info, debug

basicConfig(
    level=DEBUG,
    filename='logs.log',
    filemode='a',
    format='%(levelname)s:%(asctime)s:%(message)s;',
)

# Create your views here.
def clienteList(request):
    try:
        ClientesFor = Clientes.objects.all()
        return render(request, 'Clientes.html', {'Clientes': ClientesFor})
    except Exception as e:
        messages.warning(request, "Erro ao carregar dados por favor tente novamente mais tarde!")
        return HttpResponsePermanentRedirect(reverse('ClientesList'))
    

def ClienteView(request, pk):
    try:
        ClientesFor = Clientes.objects.get(pk=pk)
        return render(request, 'ClienteView.html', {'Clientes': ClientesFor})
    except Exception as e:
        messages.warning(request, "Erro ao carregar dados por favor tente novamente mais tarde!")
        return HttpResponsePermanentRedirect(reverse('ClientesList'))
    

def ClienteInsert(request):
    
    if request.method == 'POST' :
            print(type(request.POST["Celular"]))
            try:
                erro = 0
                if request.POST["Nome"] is None or not request.POST["Nome"]:
                    messages.warning(request, "O Nome Precisa ser preenchido!")
                    erro = 1
                    return HttpResponsePermanentRedirect(reverse('ClienteInsert'))
                
                elif Clientes.objects.filter(CNPJ_CPF=request.POST["CNPJ_CPF"]).exists():
                    messages.warning(request, "Erro esse CNPJ ou CPF já existe!")
                    erro = 1
                    return HttpResponsePermanentRedirect(reverse('ClienteInsert'))
                
                elif request.POST["CNPJ_CPF"] is None or not request.POST["CNPJ_CPF"]:
                    messages.warning(request, "O CNPJ ou CPF tem que ser preenchido!")
                    erro = 1
                    return HttpResponsePermanentRedirect(reverse('ClienteInsert'))
                
                elif validador(request.POST["CNPJ_CPF"]):
                    messages.warning(request, validador(request.POST["CNPJ_CPF"]))
                    erro = 1
                    return HttpResponsePermanentRedirect(reverse('ClienteInsert'))

                elif request.POST["Email"] is None or not request.POST["Email"]:
                    messages.warning(request, "O Email tem que ser preenchido!")
                    erro = 1
                    return HttpResponsePermanentRedirect(reverse('ClienteInsert'))
                
                elif Clientes.objects.filter(Email=request.POST["Email"]).exists():
                    messages.warning(request, "Erro esse Email já existe!")
                    erro = 1
                    return HttpResponsePermanentRedirect(reverse('ClienteInsert'))
                
                elif request.POST["Celular"] is None or not request.POST["Celular"]:
                    messages.warning(request, "O Celular tem que ser preenchido!")
                    erro = 1
                    return HttpResponsePermanentRedirect(reverse('ClienteInsert'))
                
                elif request.POST["Celular"] is None or not request.POST["Celular"]:
                    messages.warning(request, "O Celular tem que ser preenchido!")
                    erro = 1
                    return HttpResponsePermanentRedirect(reverse('ClienteInsert'))
                else: 
                    try:
                        int(request.POST["Celular"])  
                    except ValueError:
                        erro = 1
                        messages.warning(request, "Por favor Coloque apenas numeros!")
                        return HttpResponsePermanentRedirect(reverse('ClienteInsert'))
                
                if erro == 0:
                    try:

                        Cliente = Clientes()
                        Cliente.Nome = request.POST["Nome"]
                        Cliente.CNPJ_CPF = [int(digito) for digito in request.POST["CNPJ_CPF"] if digito.isdigit()]
                        Cliente.Email = request.POST["Email"]
                        Cliente.Celular = request.POST["Celular"]

                        Cliente.save()

                        messages.success(request, "Dados inseridos com sucesso!")
                        return redirect('ClientesList')
                    
                    except ValueError:
                        messages.warning(request, "Por favor Coloque apenas numeros!")
                        return HttpResponsePermanentRedirect(reverse('ClienteInsert'))
                if erro == 1:
                    messages.warning(request, "Erro ao validar os dados por favor tente mais tarde!")
                    return HttpResponsePermanentRedirect(reverse('ClientesList'))
                else:
                    messages.warning(request, f"Erro ao validar dados, por favor preencha corretamente ou tente novamente mais tarde!{e}")
                    return HttpResponsePermanentRedirect(reverse('ClientesList'))
                
                            
            except Exception as e:
                messages.warning(request, f"Erro ao validar dados, por favor preencha corretamente ou tente novamente mais tarde!{e}")
                return HttpResponsePermanentRedirect(reverse('ClienteInsert'))

    else:
        try:
            
            return render(request, 'ClientesInsert.html')
        except Exception as e:
            messages.warning(request, "Erro ao carregar dados por favor tente novamente mais tarde!")
            return HttpResponsePermanentRedirect(reverse('ClientesList'))
    

def ClienteEdit(request, pk):

    if request.method == 'POST' :
            numerosCPF = ApenasNumero(request.POST["CNPJ_CPF"])


            try:
                erro = 0
                if request.POST["Nome"] is None or not request.POST["Nome"]:
                    warning("O Nome Precisa ser preenchido!")
                    messages.warning(request, "O Nome Precisa ser preenchido!")
                    erro = 1
                    return redirect('ClienteEdit', pk)
            
                elif numerosCPF is None or not numerosCPF:
                    warning("O CNPJ ou CPF tem que ser preenchido!")
                    messages.warning(request, "O CNPJ ou CPF tem que ser preenchido!")
                    erro = 1
                    return redirect('ClienteEdit', pk)
                
                elif not len(numerosCPF) == 11:
                    warning("O CPF deve ter 11 digitos!")
                    messages.warning(request, "O CPF deve ter 11 digitos")
                    erro = 1
                    return redirect('ClienteEdit', pk)
                
                elif validador(request.POST["CNPJ_CPF"]) == 0:
                    warning("O CPF não é válido...")
                    messages.warning(request, "O CPF não é válido...")
                    erro = 1
                    return redirect('ClienteEdit', pk)

                elif request.POST["Email"] is None or not request.POST["Email"]:
                    warning("O Email tem que ser preenchido!")
                    messages.warning(request, "O Email tem que ser preenchido!")
                    erro = 1
                    return redirect('ClienteEdit', pk)
                
                elif request.POST["Celular"] is None or not request.POST["Celular"]:
                    warning("O Celular tem que ser preenchido!")
                    messages.warning(request, "O Celular tem que ser preenchido!")
                    erro = 1
                    return redirect('ClienteEdit', pk)
                

                if erro == 0:
                    Cliente = Clientes.objects.get(id=pk)
                    Cliente.Nome = request.POST["Nome"]
                    Cliente.CNPJ_CPF = numerosCPF
                    Cliente.Email = request.POST["Email"]
                    Cliente.Celular = request.POST["Celular"]
                    Cliente.save()

                    info(f"Dados Editados com sucesso!" )
                    messages.success(request, "Dados Editados com sucesso!")
                    return redirect('ClientesList')
                else:
                    warning("Erro ao validar dados, por favor preencha corretamente")
                    messages.warning(request, f"Erro ao validar dados, por favor preencha corretamente ou tente novamente mais tarde!") 
                    return redirect('ClienteEdit', pk)       
            except Exception as e:
                error(f"Erro ao tentar salvar dados No banco de dados {e}")
                messages.error(request, f"Erro ao tentar salvar dados!")
                return redirect('ClienteEdit', pk)

    else:
        try:
            Cliente = Clientes.objects.get(id=pk)
            return render(request, 'ClientesEdit.html',{'Clientes': Cliente})
        except Exception as e:
            messages.warning(request, "Erro ao carregar dados por favor tente novamente mais tarde!")
            return redirect('ClientesList')
        
    

def ClienteDelete(request, pk):

    if request.method == 'POST':
        try:
            Cliente = Clientes.objects.get(id=pk)
            Cliente.delete()
            messages.success(request, "Dados excluidos com sucesso!")
            return HttpResponsePermanentRedirect(reverse('ClientesList'))
        except Exception as e:
            messages.warning(request, "Erro ao excluir por favor tente novamente mais tarde!")
            return HttpResponsePermanentRedirect(reverse('ClienteDelete', pk))

    else:
        try:
            Cliente = Clientes.objects.get(id=pk)
            return render(request, 'ClientesDelete.html',{'Clientes': Cliente})
        except Exception as e:
            messages.warning(request, "Erro ao carregar dados por favor tente novamente mais tarde!")
            return HttpResponsePermanentRedirect(reverse('ClientesList'))