# Generated by Django 2.2 on 2019-04-14 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_template', '0003_auto_20190413_2048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producttemplate',
            name='open_stock',
        ),
    ]
