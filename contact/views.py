from django.shortcuts import render, redirect
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if forms.is_valid():
            form.save()
            return render(request, 'contact/thank_you.html')
        else: 
            form = ContactForm()
        
        return render(request, 'contact/contact.html', {'form': form})
