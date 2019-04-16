from django import forms
from backend.models import Category, SubCategory


class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = "__all__"
        choices = (('Active', 'Active'), ('Inactive', 'Inactive'))
        category = Category.objects.all()
        widgets = {
            'category_name': forms.Select(choices=category, attrs={'class': 'form-control'}),
            'sub_category_name': forms.TextInput(attrs={'class': 'form-control'}),
            'sub_category_code': forms.NumberInput(attrs={'class': 'form-control'}),
            'sub_category_description': forms.Textarea(attrs={'class': 'form-control'}),
            'sub_category_status': forms.Select(choices=choices, attrs={'class': 'form-control'})
        }
