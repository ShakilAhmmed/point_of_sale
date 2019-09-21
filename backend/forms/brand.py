from django import forms
from backend.models import Company


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = "__all__"
        choices = (('Active', 'Active'), ('Inactive', 'Inactive'))
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'company_code': forms.NumberInput(attrs={'class': 'form-control'}),
            'company_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'company_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'company_address': forms.Textarea(attrs={'class': 'form-control', 'rows': '2'}),
            'company_status': forms.Select(choices=choices, attrs={'class': 'form-control'}),
            'company_notify': forms.CheckboxInput(attrs={'class': 'custom-control-input select_all_child'}),
        }
