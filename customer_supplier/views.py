from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from .forms.customer import CustomerForm, CustomerAddressForm


@login_required
def customer(request):
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST, request.FILES)
        customer_address_form = CustomerAddressForm(request.POST)
        if customer_form.is_valid():
            customer_save = customer_form.save()
            customer_address_save = customer_address_form.save(commit=False)
            customer_address_save.customer = customer_save
            if customer_address_form.is_valid():
                customer_address_save.save()
            messages.success(request, 'Customer Added Successfully')
            return HttpResponseRedirect(reverse('customer'))
    else:
        customer_form = CustomerForm()
        customer_address_form = CustomerAddressForm()
    context = {
        'customer_form': customer_form,
        'customer_address_form': customer_address_form
    }
    return render(request, 'backend/Customer_Supplier/customer.html', context)


@login_required
def customer_report(request):
    return render(request, 'backend/Customer_Supplier/customer_report.html')


@login_required
def supplier(request):
    return render(request, 'backend/Customer_Supplier/supplier.html')


@login_required
def supplier_report(request):
    return render(request, 'backend/Customer_Supplier/supplier_report.html')
