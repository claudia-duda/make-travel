from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from .class_type import type_classes
from .validation import *

class PassagemForms(forms.Form):
    origem = forms.CharField(label='Origem', max_length=100) 
    destino = forms.CharField(label='Destino', max_length=100)
    ida = forms.DateField(label='Data ida', widget=DatePicker())
    volta= forms.DateField(label='Data volta', widget=DatePicker())
    pesquisa_data= forms.DateField(label='Data da pesquisa', disabled=True, initial=datetime.today)
    class_type = forms.ChoiceField(label = 'Tipo de classe', choices=type_classes)
    informacoes = forms.CharField(label ='Informações extras', required=False, max_length=200, widget= forms.Textarea())
    email= forms.EmailField(label="Seu email", max_length=150)

    def clean(self):
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        ida = self.cleaned_data.get('ida')
        volta = self.cleaned_data.get('volta')
        pesquisa_data = self.cleaned_data.get('pesquisa_data')

        lista_de_erros = {}
        campo_tem_algum_numero(origem,'origem',lista_de_erros)
        campo_tem_algum_numero(destino, 'destino', lista_de_erros)
        origem_destino_iguais(origem,destino,lista_de_erros)
        data_ida_maior_que_data_volta(ida,volta,lista_de_erros)
        data_ida_menor_data_de_hoje(ida,pesquisa_data,lista_de_erros)

        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem = lista_de_erros[erro]
                self.add_error(erro, mensagem) 
        return self.cleaned_data