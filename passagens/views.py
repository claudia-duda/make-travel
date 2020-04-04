from django.shortcuts import render
from passagens.forms import PassagemForms
# Create your views here.

def index(request):
    form = PassagemForms()
    return render(request, 'passagens/index.html', {'form':form})

def travels(request):
    if request.method == 'POST':
      #  if(form.is_valid()):
            form = PassagemForms(request.POST)  #pega as informações digitadas
            return render(request, 'passagens/list-travel.html', {'form':form})  
   # else:
   #     form = PassagemForms()
    


 