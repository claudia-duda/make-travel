from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from .validation import *
from .models import Passagem, Pessoa, Classes

class PassagemForms(forms.ModelForm):

    data_pesquisa = forms.DateField(label='Data da pesquisa', disabled=True, initial=datetime.today)

    class Meta:
        model = Passagem
        fields= '__all__'
        labels={'ida': 'Data de ida', 'volta': 'Data de volta','informacoes': 'Informações adicionais', 'classe':'Classe do voô'}
        widgets = {
            'ida': DatePicker(),
            'volta': DatePicker()
        }
        

        def clean(self):
            origem = self.cleaned_data.get('origem')
            destino = self.cleaned_data.get('destino')
            ida = self.cleaned_data.get('ida')
            volta = self.cleaned_data.get('volta')
            pesquisa_data = self.cleaned_data.get('data_pesquisa')

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

class PessoaForms(forms.ModelForm):
    class Meta:
        model = Pessoa
        exclude = ['nome']             