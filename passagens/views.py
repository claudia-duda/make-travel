from django.shortcuts import render
from .forms import PassagemForms
# Create your views here.

def index(request):
    form = PassagemForms()
    return render(request, 'passagens/index.html', {'form':form})

def travels(request):
    if request.method == 'POST':
        form = PassagemForms(request.POST)  #pega as informações digitadas
        if form.is_valid():            
            return render(request, 'passagens/list-travel.html', {'form':form})  
        else:
            return render(request, 'passagens/index.html', {'form': form})
    


 