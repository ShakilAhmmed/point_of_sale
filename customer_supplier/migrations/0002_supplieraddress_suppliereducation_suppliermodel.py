# Generated by Django 2.2 on 2019-04-19 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer_supplier', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupplierModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_name', models.CharField(max_length=100)),
                ('supplier_code', models.IntegerField(unique=True)),
                ('supplier_phone', models.CharField(max_length=20, unique=True)),
                ('supplier_email', models.EmailField(max_length=254, unique=True)),
                ('supplier_account_no', models.CharField(max_length=100, unique=True)),
                ('supplier_status', models.CharField(max_length=15)),
                ('supplier_notify', models.BooleanField(max_length=3)),
                ('supplier_profile_picture', models.ImageField(default='company/blank.png', upload_to='supplier/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SupplierEducation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_exam_name', models.CharField(max_length=100)),
                ('supplier_board_name', models.CharField(max_length=100)),
                ('supplier_passing_year', models.CharField(max_length=100)),
                ('supplier_department_name', models.CharField(max_length=100)),
                ('supplier_result', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer_supplier.SupplierModel')),
            ],
        ),
        migrations.CreateModel(
            name='SupplierAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_post_office', models.CharField(max_length=100)),
                ('supplier_home_district', models.CharField(max_length=100)),
                ('supplier_division', models.CharField(max_length=100)),
                ('supplier_village_name', models.CharField(max_length=100)),
                ('supplier_home_name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer_supplier.SupplierModel')),
            ],
        ),
    ]
