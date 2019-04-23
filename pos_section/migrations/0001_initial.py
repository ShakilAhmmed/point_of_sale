# Generated by Django 2.2 on 2019-04-23 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product_template', '0005_auto_20190414_1512'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartParentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100)),
                ('customer', models.CharField(max_length=50)),
                ('invoice_id', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CartProductModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_id', models.CharField(max_length=150)),
                ('product_price', models.CharField(max_length=100)),
                ('product_quantity', models.CharField(max_length=100)),
                ('product_subtotal', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cart_parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pos_section.CartParentModel')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product_template.ProductTemplate')),
            ],
        ),
        migrations.CreateModel(
            name='CartPaymentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_id', models.CharField(max_length=150)),
                ('total', models.CharField(max_length=150)),
                ('pay', models.CharField(max_length=150)),
                ('change_due', models.CharField(blank=True, max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cart_parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pos_section.CartParentModel')),
            ],
        ),
    ]