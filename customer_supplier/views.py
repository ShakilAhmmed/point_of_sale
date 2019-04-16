from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
@login_required
def customer(request):
    return render(request, 'backend/Customer_Supplier/customer.html')


@login_required
def customer_report(request):
    return render(request, 'backend/Customer_Supplier/customer_report.html')


@login_required
def supplier(request):
    return render(request, 'backend/Customer_Supplier/supplier.html')


@login_required
def supplier_report(request):
    return render(request, 'backend/Customer_Supplier/supplier_report.html')
