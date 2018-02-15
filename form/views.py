from django.shortcuts import render
from .forms import NumberForm
import re

def numbers_send(request):
    sent = False
    if request.method == 'POST':
        sent = True
        form= NumberForm(request.POST)
        if form.is_valid():
                cd = form.cleaned_data
                numbers= cd['numbers']
                ptr = r'(\d+)'
                if re.match(ptr,numbers):
                    n= numbers.split(",")
                    n.sort()
                    numbers = ","
                    message = numbers.join(n)

    else:
        message = 'Nic sie nie dzieje'
        form = NumberForm()
    return render(request, 'form/templates/form/index.html', {'sent': sent,'message': message, 'form':form})
