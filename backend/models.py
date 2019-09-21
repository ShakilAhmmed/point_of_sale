from django.db import models


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    category_code = models.IntegerField(unique=True)
    category_description = models.TextField()
    category_status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name


class SubCategory(models.Model):
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    sub_category_name = models.CharField(max_length=50, unique=True)
    sub_category_code = models.IntegerField(unique=True)
    sub_category_description = models.TextField()
    sub_category_status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Company(models.Model):
    company_name = models.CharField(max_length=50, unique=True)
    company_code = models.IntegerField(unique=True)
    company_phone = models.CharField(max_length=15)
    company_email = models.EmailField(max_length=50)
    company_address = models.TextField()
    company_status = models.CharField(max_length=10)
    company_notify = models.BooleanField()
    company_logo = models.ImageField(upload_to='company/', default='company/blank.png')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name


class Setup(models.Model):
    company_name = models.CharField(max_length=100)
    company_email = models.EmailField(max_length=100)
    company_address = models.TextField()
    company_phone = models.CharField(max_length=20)
    company_logo = models.ImageField(upload_to="setup/", default='company/blank.png')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
