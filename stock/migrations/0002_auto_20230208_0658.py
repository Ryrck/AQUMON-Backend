# Generated by Django 3.2.17 on 2023-02-08 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='Stock_price',
            new_name='stock_price',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='Stock_symbol',
            new_name='stock_symbol',
        ),
    ]
