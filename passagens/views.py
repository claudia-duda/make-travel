from django.shortcuts import render
from .forms import PessoaForms, PassagemForms
# Create your views here.

def index(request):
    form = PassagemForms()
    pessoaForm = PessoaForms()
    return render(request, 'passagens/index.html', {'form': form , 'pessoaForm': pessoaForm})

def travels(request):
    if request.method == 'POST':
        form = PassagemForms(request.POST)  #pega as informações digitadas da passagem
        pessoaForm = PessoaForms(request.POST)
        if form.is_valid():            
            return render(request, 'passagens/list-travel.html', {'form':form , 'pessoaForm': pessoaForm})  
        else:
            return render(request, 'passagens/index.html', {'form': form , 'pessoaForm': pessoaForm})
    


 