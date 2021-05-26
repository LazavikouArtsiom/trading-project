# Generated by Django 3.1.11 on 2021-05-25 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0002_auto_20210525_0649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='purchase_quantity_after_trade',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trade',
            name='purchase_quantity_before_trade',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trade',
            name='sale_quantity_after_trade',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trade',
            name='sale_quantity_before_trade',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
