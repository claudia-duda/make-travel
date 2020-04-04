from django import forms
from tempus_dominus.widgets import DatePicker

class PassagemForms(forms.Form):
    origem = forms.CharField(label='Origem', max_length=100) 
    destino = forms.CharField(label='Destino', max_length=100)
    ida = forms.DateField(label='ida', widget=DatePicker())
    volta= forms.DateField(label='volta', widget=DatePicker())