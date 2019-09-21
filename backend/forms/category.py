from django import forms
from backend.models import Category


class CategoryForm(forms.ModelForm):
    category_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    category_code = forms.CharField(max_length=50, widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))
    category_description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
    }))

    CHOICES = (('Active', 'Active'), ('Inactive', 'Inactive'))
    category_status = forms.CharField(max_length=20, widget=forms.Select(choices=CHOICES, attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = Category
        fields = "__all__"
