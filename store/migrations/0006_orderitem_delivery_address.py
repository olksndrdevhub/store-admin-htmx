# Generated by Django 4.2 on 2023-11-29 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_rename_completed_order_payment_completed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='delivery_address',
            field=models.TextField(blank=True, null=True),
        ),
    ]