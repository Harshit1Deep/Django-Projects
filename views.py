from django.shortcuts import render,HttpResponse
from datetime import datetime
from website.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    messages.success(request," This is a test message")
    return render(request,'index.html')
    # return HttpResponse("This is home page")
def about(request):
    return render(request,'about.html')
    
def services(request):
    return render(request,'services.html')
    
def contact(request):
    if request.method == "POST":
        name =    request.POST.get('name')
        email =   request.POST.get('email')
        amount =  request.POST.get('amount')
        message = request.POST.get('message')
        contact = Contact(name=name,email=email,amount=amount,message=message,date=datetime.today())
        contact.save()
        messages.success(request,"Details uploaded")
    return render(request,'contact.html')
    
