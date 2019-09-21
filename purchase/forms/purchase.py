from django import forms

from purchase.models import PurchaseModel


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = PurchaseModel
        fields = "__all__"
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control datepicker date', 'style': 'width: 200px;'}),
            'company_name': forms.Select(attrs={'class': 'form-control company_name', 'style': "width: 200px;margin-left:-14px;"}),
            'supplier_name': forms.Select(attrs={'class': 'form-control supplier_name', 'style': 'width: 200px;margin-left:-10px;'})
        }



