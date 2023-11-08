from django.shortcuts import render
from .models import Contact
# Create your views here.
def page2(request):
    return render(request, "contact/page2.html")

def createcontact(request):
    return render(request, "contact/createcontact.html")



def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contact/contactlist.html', {'contacts': contacts})