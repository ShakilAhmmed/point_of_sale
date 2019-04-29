from django import forms

from backend.models import Setup


class SetupForm(forms.ModelForm):
    class Meta:
        model = Setup
        fields = "__all__"
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'company_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'company_address': forms.Textarea(attrs={'class': 'form-control', 'rows': '2'}),
            'company_phone': forms.TextInput(attrs={'class': 'form-control'}),
        }