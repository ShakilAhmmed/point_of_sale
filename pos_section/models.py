from django.db import models

from product_template.models import ProductTemplate


class CartParentModel(models.Model):
    date = models.CharField(max_length=100)
    customer = models.CharField(max_length=50)
    invoice_id = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CartProductModel(models.Model):
    cart_parent = models.ForeignKey(CartParentModel, on_delete=models.CASCADE)
    invoice_id = models.CharField(max_length=150)
    product = models.ForeignKey(ProductTemplate, on_delete=models.DO_NOTHING)
    product_price = models.CharField(max_length=100)
    product_quantity = models.CharField(max_length=100)
    product_subtotal = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CartPaymentModel(models.Model):
    cart_parent = models.ForeignKey(CartParentModel, on_delete=models.CASCADE)
    invoice_id = models.CharField(max_length=150)
    total = models.CharField(max_length=150)
    pay = models.CharField(max_length=150)
    change_due = models.CharField(max_length=150, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)