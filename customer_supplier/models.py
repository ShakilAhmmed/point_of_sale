from django.db import models


# Create your models here.
class CustomerModel(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_code = models.CharField(max_length=100, unique=True)
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


class SupplierModel(models.Model):
    supplier_name = models.CharField(max_length=100)
    supplier_code = models.CharField(max_length=100,unique=True)
    supplier_phone = models.CharField(max_length=20, unique=True)
    supplier_email = models.EmailField(unique=True)
    supplier_account_no = models.CharField(max_length=100, unique=True)
    supplier_status = models.CharField(max_length=15)
    supplier_notify = models.BooleanField(max_length=3)
    supplier_profile_picture = models.ImageField(upload_to='supplier/', default='company/blank.png')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SupplierAddress(models.Model):
    supplier = models.ForeignKey(SupplierModel, on_delete=models.CASCADE)
    supplier_post_office = models.CharField(max_length=100)
    supplier_home_district = models.CharField(max_length=100)
    supplier_division = models.CharField(max_length=100)
    supplier_village_name = models.CharField(max_length=100)
    supplier_home_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SupplierEducation(models.Model):
    supplier = models.ForeignKey(SupplierModel, on_delete=models.CASCADE)
    supplier_exam_name = models.CharField(max_length=100)
    supplier_board_name = models.CharField(max_length=100)
    supplier_passing_year = models.CharField(max_length=100)
    supplier_department_name = models.CharField(max_length=100)
    supplier_result = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
