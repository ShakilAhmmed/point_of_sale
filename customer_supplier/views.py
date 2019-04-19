import os

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse

from .forms.customer import CustomerForm, CustomerAddressForm
from .forms.supplier import SupplierForm, SupplierAddressForm, SupplierEducationForm
from .models import CustomerModel, CustomerAddressModel, SupplierModel, SupplierAddress, SupplierEducation


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
    customer_data = CustomerModel.objects.all()
    context = {
        'customer_data': customer_data
    }
    return render(request, 'backend/Customer_Supplier/customer_report.html', context)


@login_required
def customer_status(request, pk):
    customer_data = get_object_or_404(CustomerModel, pk=pk)
    if customer_data.customer_status == 'Active':
        customer_data.customer_status = 'Inactive'
        messages.info(request, 'Status Changed Into Inactive')
    else:
        customer_data.customer_status = 'Active'
        messages.success(request, 'Status Changed Into Active')
    customer_data.save()
    return HttpResponseRedirect(reverse('customer_report'))


@login_required
def customer_edit(request, pk):
    customer_data = get_object_or_404(CustomerModel, pk=pk)
    customer_address_data = get_object_or_404(CustomerAddressModel, customer=pk)
    customer_profile_image = customer_data.customer_profile_picture
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST, request.FILES, instance=customer_data)
        customer_address_form = CustomerAddressForm(request.POST, instance=customer_address_data)
        if request.FILES:
            new_file = request.FILES.get('customer_profile_picture')
            if not customer_profile_image == new_file:
                if os.path.isfile(customer_profile_image.path):
                    os.remove(customer_profile_image.path)

        if customer_form.is_valid():
            customer_save = customer_form.save()
            customer_address_save = customer_address_form.save(commit=False)
            customer_address_save.customer = customer_save
            if customer_address_form.is_valid():
                customer_address_save.save()
            messages.success(request, 'Customer Added Successfully')
            return redirect('customer_edit', pk=pk)
    else:
        customer_form = CustomerForm(instance=customer_data)
        customer_address_form = CustomerAddressForm(instance=customer_address_data)
    if customer_profile_image:
        image = customer_profile_image.url
    else:
        image = ''
    context = {
        'customer_form': customer_form,
        'customer_address_form': customer_address_form,
        'image': image
    }
    return render(request, 'backend/Customer_Supplier/customer.html', context)


@login_required
def customer_delete(request, pk):
    customer_data = get_object_or_404(CustomerModel, pk=pk)
    if customer_data.customer_profile_picture:
        if os.path.isfile(customer_data.customer_profile_picture.path):
            os.remove(customer_data.customer_profile_picture.path)
    customer_data.delete()
    return HttpResponseRedirect(reverse('customer_report'))


@login_required
def supplier(request):
    if request.method == 'POST':
        supplier_form = SupplierForm(request.POST, request.FILES)
        supplier_address_form = SupplierAddressForm(request.POST)
        supplier_education_form = SupplierEducationForm(request.POST)
        if supplier_form.is_valid():
            new_supplier = supplier_form.save()
            new_supplier_address_form = supplier_address_form.save(commit=False)
            new_supplier_education_form = supplier_education_form.save(commit=False)
            new_supplier_address_form.supplier = new_supplier
            new_supplier_education_form.supplier = new_supplier
            if supplier_address_form.is_valid():
                supplier_address_form.save()
            if supplier_education_form.is_valid():
                supplier_education_form.save()
            messages.success(request, 'Supplier Added Successfully')
            return HttpResponseRedirect(reverse('supplier'))

    else:
        supplier_form = SupplierForm()
        supplier_address_form = SupplierAddressForm()
        supplier_education_form = SupplierEducationForm()
    context = {
        'supplier_form': supplier_form,
        'supplier_address_form': supplier_address_form,
        'supplier_education_form': supplier_education_form
    }
    return render(request, 'backend/Customer_Supplier/supplier.html', context)


@login_required
def supplier_report(request):
    supplier_data = SupplierModel.objects.all()
    context = {
        'supplier_data': supplier_data
    }
    return render(request, 'backend/Customer_Supplier/supplier_report.html', context)


@login_required
def supplier_status(request, pk):
    supplier_data = get_object_or_404(SupplierModel, pk=pk)
    if supplier_data.supplier_status == 'Active':
        supplier_data.supplier_status = 'Inactive'
        messages.info(request, 'Status Changed Into Inactive')
    else:
        supplier_data.supplier_status = 'Active'
        messages.success(request, 'Status Changed Into Active')
    supplier_data.save()
    return HttpResponseRedirect(reverse('supplier_report'))


@login_required
def supplier_edit(request, pk):
    supplier_data = get_object_or_404(SupplierModel, pk=pk)
    supplier_address = get_object_or_404(SupplierAddress, supplier=pk)
    supplier_education = get_object_or_404(SupplierEducation, supplier=pk)
    old_file = supplier_data.supplier_profile_picture
    if request.method == 'POST':
        supplier_form = SupplierForm(request.POST, request.FILES, instance=supplier_data)
        supplier_address_form = SupplierAddressForm(request.POST, instance=supplier_address)
        supplier_education_form = SupplierEducationForm(request.POST, instance=supplier_education)
        if supplier_form.is_valid():
            if request.FILES:
                new_file = request.FILES.get('supplier_profile_picture')
                if not old_file == new_file:
                    if os.path.isfile(old_file.path):
                        os.remove(old_file.path)
            new_supplier = supplier_form.save()
            new_supplier_address_form = supplier_address_form.save(commit=False)
            new_supplier_education_form = supplier_education_form.save(commit=False)
            new_supplier_address_form.supplier = new_supplier
            new_supplier_education_form.supplier = new_supplier
            if supplier_address_form.is_valid():
                supplier_address_form.save()
            if supplier_education_form.is_valid():
                supplier_education_form.save()
            messages.success(request, 'Supplier Added Successfully')
            return redirect('supplier_edit',pk=pk)

    else:
        supplier_form = SupplierForm(instance=supplier_data)
        supplier_address_form = SupplierAddressForm(instance=supplier_address)
        supplier_education_form = SupplierEducationForm(instance=supplier_education)
    if supplier_data.supplier_profile_picture:
        image = supplier_data.supplier_profile_picture.url
    else:
        image = ''
    context = {
        'supplier_form': supplier_form,
        'supplier_address_form': supplier_address_form,
        'supplier_education_form': supplier_education_form,
        'image': image
    }
    return render(request, 'backend/Customer_Supplier/supplier.html', context)


@login_required
def supplier_delete(request, pk):
    supplier_data = get_object_or_404(SupplierModel, pk=pk)
    if supplier_data.supplier_profile_picture:
        if os.path.isfile(supplier_data.supplier_profile_picture.path):
            os.remove(supplier_data.supplier_profile_picture.path)
    supplier_data.delete()
    messages.info(request, 'Supplier Deleted Successfully')
    return HttpResponseRedirect(reverse('supplier_report'))
