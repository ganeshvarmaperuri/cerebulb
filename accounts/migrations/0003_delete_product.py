# Generated by Django 3.1.4 on 2021-02-16 02:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_product_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
    ]