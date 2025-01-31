# Generated by Django 5.1.4 on 2024-12-16 04:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
        ('stor', '0006_product_pdf_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='order',
            name='total',
        ),
        migrations.AddField(
            model_name='order',
            name='transaction',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='checkout.transaction'),
        ),
    ]
