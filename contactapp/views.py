from django.shortcuts import render

# Create your views here.
def page2(request):
    return render(request, "contact/page2.html")

def createcontact(request):
    return render(request, "contact/createcontact.html")

