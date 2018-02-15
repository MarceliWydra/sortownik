from django.shortcuts import render
from .forms import NumberForm
import re

def numbers_send(request):
    sent = False
    message = 0
    if request.method == 'POST':
        sent = True
        form= NumberForm(request.POST)
        if form.is_valid():
                cd = form.cleaned_data
                numbers= cd['numbers']
                n = numbers.replace(',','')
                if n.isdigit():
                    n= numbers.split(",")
                    n.sort(key=int)
                    numbers = ","
                    message = numbers.join(n)
                else:
                    message = 'Złe dane!'
    else:
        form = NumberForm()
    return render(request, 'form/templates/form/index.html', {'sent': sent,'message': message, 'form':form})
