from django import forms

from customer_supplier.models import CustomerModel, CustomerAddressModel


class CustomerForm(forms.ModelForm):
    class Meta:
        model = CustomerModel
        fields="__all__"
        choices = (('Active', 'Active'), ('Inactive', 'Inactive'))
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_code': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_email': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_account_no': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_discount': forms.NumberInput(attrs={'class': 'form-control'}),
            'customer_status': forms.Select(choices=choices, attrs={'class': 'form-control'}),
            'customer_notify': forms.CheckboxInput(attrs={'class': 'custom-control-input select_all_child'}),
            'customer_taxable': forms.CheckboxInput(attrs={'class': 'custom-control-input select_all_child'}),
        }


class CustomerAddressForm(forms.ModelForm):
    class Meta:
        model = CustomerAddressModel
        exclude = ("customer",)
        widgets = {
            'customer_post_office': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_home_district': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_division': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_village_name': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_home_name': forms.TextInput(attrs={'class': 'form-control'}),
        }
