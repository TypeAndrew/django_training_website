from django import forms

class OrderForm(forms.Form)
    name = forms.CharField(max_length=200)
    phone  = forms.CharField(max_length=200)