from django.db import models
from backend.models import Category, SubCategory, Company


# Create your models here.
class ProductTemplate(models.Model):
    product_name = models.CharField(max_length=100)
    product_code = models.CharField(max_length=100, unique=True)
    product_brand_name = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    product_cost_price = models.PositiveIntegerField()
    product_mrp = models.PositiveIntegerField()
    product_tax = models.FloatField(max_length=50)
    product_unit = models.CharField(max_length=50)
    product_description = models.TextField()
    product_status = models.CharField(max_length=20)
    is_published = models.BooleanField(max_length=5)
    cover_image = models.ImageField(upload_to="product_template/cover/", default="company/blank.png")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

class ProductTemplateCategory(models.Model):
    product_template = models.ForeignKey(ProductTemplate, on_delete=models.CASCADE)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ProductTemplateSubCategory(models.Model):
    product_template = models.ForeignKey(ProductTemplate, on_delete=models.CASCADE)
    product_sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ProductTemplateImages(models.Model):
    product_template = models.ForeignKey(ProductTemplate, on_delete=models.CASCADE)
    product_image_title = models.CharField(max_length=100)
    product_image = models.ImageField(upload_to="product_template/other/", default="company/blank.png")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
