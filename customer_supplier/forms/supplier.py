from django import forms

from customer_supplier.models import SupplierModel, SupplierAddress, SupplierEducation


class SupplierForm(forms.ModelForm):
    class Meta:
        model = SupplierModel
        fields = "__all__"
        choices = (('Active', 'Active'), ('Inactive', 'Inactive'))
        widgets = {
            'supplier_name': forms.TextInput(attrs={'class': 'form-control'}),
            'supplier_code': forms.TextInput(attrs={'class': 'form-control'}),
            'supplier_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'supplier_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'supplier_account_no': forms.TextInput(attrs={'class': 'form-control'}),
            'supplier_status': forms.Select(choices=choices, attrs={'class': 'form-control'}),
            'supplier_notify': forms.CheckboxInput(attrs={'class': 'custom-control-input select_all_child'}),
        }


class SupplierAddressForm(forms.ModelForm):
    class Meta:
        model = SupplierAddress
        exclude = ("supplier",)
        widgets = {
            'supplier_post_office': forms.TextInput(attrs={'class': 'form-control'}),
            'supplier_home_district': forms.TextInput(attrs={'class': 'form-control'}),
            'supplier_division': forms.TextInput(attrs={'class': 'form-control'}),
            'supplier_village_name': forms.TextInput(attrs={'class': 'form-control'}),
            'supplier_home_name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class SupplierEducationForm(forms.ModelForm):
    class Meta:
        model = SupplierEducation
        exclude = ("supplier",)
        widgets = {
            'supplier_exam_name': forms.TextInput(attrs={'class': 'form-control'}),
            'supplier_board_name': forms.TextInput(attrs={'class': 'form-control'}),
            'supplier_passing_year': forms.TextInput(attrs={'class': 'form-control'}),
            'supplier_department_name': forms.TextInput(attrs={'class': 'form-control'}),
            'supplier_result': forms.TextInput(attrs={'class': 'form-control'}),
        }
