from django import forms

from product_template.models import ProductTemplate, ProductTemplateImages, ProductTemplateCategory, ProductTemplateSubCategory

from backend.models import Company


class ProductTemplateForm(forms.ModelForm):
    class Meta:
        model = ProductTemplate
        fields = "__all__"
        brand = Company.objects.filter(company_status='Active')
        status_choice = (('Active', 'Active'), ('Inactive', 'Inactive'))
        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-control'}),
            'product_code': forms.TextInput(attrs={'class': 'form-control'}),
            'product_brand_name': forms.Select(choices=brand, attrs={'class': 'form-control'}),
            'product_cost_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'product_mrp': forms.NumberInput(attrs={'class': 'form-control'}),
            'product_tax': forms.NumberInput(attrs={'class': 'form-control'}),
            'product_unit': forms.TextInput(attrs={'class': 'form-control'}),
            'product_description': forms.Textarea(attrs={'class': 'form-control', 'rows': '2'}),
            'product_status': forms.Select(choices=status_choice, attrs={'class': 'form-control'}),
            'is_published': forms.CheckboxInput(attrs={'class': 'custom-control-input select_all_child'})
        }


class ProductTemplateCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductTemplateCategory
        fields = "__all__"


class ProductTemplateSubCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductTemplateSubCategory
        fields = "__all__"


class ProductTemplateImageForm(forms.ModelForm):
    class Meta:
        model = ProductTemplateImages
        fields = "__all__"
