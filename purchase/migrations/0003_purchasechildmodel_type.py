# Generated by Django 2.2 on 2019-04-19 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0002_remove_purchasechildmodel_tax'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchasechildmodel',
            name='type',
            field=models.CharField(default='Packet', max_length=10),
        ),
    ]
