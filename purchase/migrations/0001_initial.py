# Generated by Django 2.2 on 2019-04-19 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('backend', '0002_auto_20190416_1953'),
        ('product_template', '0005_auto_20190414_1512'),
        ('customer_supplier', '0003_auto_20190419_0925'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseChildModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('tax', models.FloatField()),
                ('sub_total', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product_template.ProductTemplate')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('company_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='backend.Company')),
                ('supplier_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='customer_supplier.SupplierModel')),
            ],
        ),
        migrations.CreateModel(
            name='PurchasePaymentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.PositiveIntegerField()),
                ('pay', models.PositiveIntegerField()),
                ('due', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchase.PurchaseModel')),
                ('purchase_child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchase.PurchaseChildModel')),
            ],
        ),
        migrations.AddField(
            model_name='purchasechildmodel',
            name='purchase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchase.PurchaseModel'),
        ),
    ]
