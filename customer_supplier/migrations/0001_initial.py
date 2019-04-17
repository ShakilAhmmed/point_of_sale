# Generated by Django 2.2 on 2019-04-16 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_code', models.CharField(max_length=100, unique=True)),
                ('customer_phone', models.CharField(max_length=20)),
                ('customer_email', models.EmailField(max_length=254, unique=True)),
                ('customer_account_no', models.CharField(max_length=100, unique=True)),
                ('customer_discount', models.IntegerField()),
                ('customer_status', models.CharField(max_length=20)),
                ('customer_notify', models.BooleanField(max_length=3)),
                ('customer_taxable', models.BooleanField(max_length=3)),
                ('customer_profile_picture', models.ImageField(default='company/blank.png', upload_to='customer/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerAddressModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_post_office', models.CharField(max_length=100)),
                ('customer_home_district', models.CharField(max_length=100)),
                ('customer_division', models.CharField(max_length=100)),
                ('customer_village_name', models.CharField(max_length=100)),
                ('customer_home_name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer_supplier.CustomerModel')),
            ],
        ),
    ]
