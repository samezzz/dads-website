from django.shortcuts import render, redirect
from . models import *
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "index.html")

def contact(request):
    if request.method == "POST":
        new_partner = Message(
            name = request.POST['name'],
            email = request.POST['email'],
            phone_number = request.POST['number'],
            description = request.POST['message'],
        )
        new_partner.save()
        return redirect('contact')
    
    return render(request, 'contact.html')

def products(request):
    return render(request, 'products.html')