from django.db import models


# Create your models here.
class CustomerModel(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_code = models.CharField(max_length=100,unique=True)
    customer_phone = models.CharField(max_length=20)
    customer_email = models.EmailField(unique=True)
    customer_account_no = models.CharField(max_length=100, unique=True)
    customer_discount = models.IntegerField()
    customer_status = models.CharField(max_length=20)
    customer_notify = models.BooleanField(max_length=3)
    customer_taxable = models.BooleanField(max_length=3)
    customer_profile_picture = models.ImageField(upload_to='customer/', default='company/blank.png')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CustomerAddressModel(models.Model):
    customer = models.ForeignKey(CustomerModel, on_delete=models.CASCADE)
    customer_post_office = models.CharField(max_length=100)
    customer_home_district = models.CharField(max_length=100)
    customer_division = models.CharField(max_length=100)
    customer_village_name = models.CharField(max_length=100)
    customer_home_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
