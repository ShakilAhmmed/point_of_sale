# Generated by Django 2.2 on 2019-04-19 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchasechildmodel',
            name='tax',
        ),
    ]
