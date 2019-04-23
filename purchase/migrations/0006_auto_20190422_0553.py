# Generated by Django 2.2 on 2019-04-22 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0005_stockmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasechildmodel',
            name='product_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_template.ProductTemplate'),
        ),
        migrations.AlterField(
            model_name='purchasemodel',
            name='company_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Company'),
        ),
    ]