from django.shortcuts import render, get_object_or_404, redirect
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

def contact_detail(request, serial_number):
    contact = get_object_or_404(Contact, serial_number=serial_number)
    return render(request, 'contact/contact_detail.html', {'contact': contact})


def update_contact(request, serial_number):
    contact = get_object_or_404(Contact, serial_number=serial_number)

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('startpage')
    else:
        form = ContactForm(instance=contact)

    return render(request, 'contact/update_contact.html', {'form': form, 'contact': contact})


def delete_contact(request, serial_number):
    contact = get_object_or_404(Contact, serial_number=serial_number)

    if request.method == 'POST':
        contact.delete()
        return redirect('startpage')

    return render(request, 'contact/delete_contact.html', {'contact': contact})