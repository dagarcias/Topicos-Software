from django import forms
from. import models


class carritoform(forms.Form):
    codigo=forms.CharField(label='codigo', max_length=6, min_length=6)
    tipoDePrenda=forms.CharField(label='tipoDePrenda')


    