from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'home.html')

def benefits(request):
    return render(request,'benefits.html')

def card(request):
    return render(request,'card.html')

def CustomerManagement(request):
    return render(request,'customer-management.html')

def featurepage(request):
    return render(request,'featurepage.html')

def login(request):
    return render(request,'login.html')

def vlog(request):
    return render(request,'vlog.html')

def contactus(request):
    return render(request,'contactus.html')

def ecommerce(request):
    return render(request,'ecommerce.html')

def StoredValueCards(request):
    return render(request,'stored-value-cards.html')

def POS3(request):
    return render(request,'POS3.html')

def inventory(request):
    return render(request,'inventory.html')

def StaffManagement(request):
    return render(request,'staff-management.html')

def shipping(request):
    return render(request,'shipping.html')


    
