from django.shortcuts import render, redirect
from .forms import CustomerForm
from .models import Customer

def home(request):
    return render(request, 'pages/home.html')   

def customers(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customers')

    customers = Customer.objects.all()
    form = CustomerForm()
    return render(request, 'pages/customers.html', {'form': form, 'customers': customers})

def shipments(request):
    return render(request, 'pages/shipments.html')