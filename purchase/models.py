from django.db import models

# Create your models here.
from backend.models import Company

# Create your models here.
from customer_supplier.models import SupplierModel

from product_template.models import ProductTemplate


class PurchaseModel(models.Model):
    date = models.DateField()
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE)
    supplier_name = models.ForeignKey(SupplierModel, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PurchaseChildModel(models.Model):
    purchase = models.ForeignKey(PurchaseModel, on_delete=models.CASCADE)
    product_name = models.ForeignKey(ProductTemplate, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    sub_total = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PurchasePaymentModel(models.Model):
    purchase = models.ForeignKey(PurchaseModel, on_delete=models.CASCADE)
    purchase_child = models.ForeignKey(PurchaseChildModel, on_delete=models.CASCADE)
    total = models.PositiveIntegerField()
    pay = models.PositiveIntegerField()
    due = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class StockModel(models.Model):
    purchase = models.ForeignKey(PurchaseModel, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductTemplate, on_delete=models.CASCADE)
    stock_code = models.CharField(max_length=256, unique=True)
    stock_status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
