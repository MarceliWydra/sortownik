from django import forms

class NumberForm(forms.Form):
    numbers = forms.CharField(label="", widget= forms.TextInput(attrs={'class':'p-2', 'name': 'numbers', 'style': 'width:100%',}))
