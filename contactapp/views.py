from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm

def startpage(request):
    contacts = Contact.objects.all()
    return render(request, 'contact/startpage.html', {'contacts': contacts})

def create_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('startpage')
    else:
        form = ContactForm()

    return render(request, 'contact/create_contact.html', {'form': form})
