# Generated by Django 3.1.11 on 2021-05-26 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0007_auto_20210524_1447'),
        ('trades', '0004_auto_20210526_0853'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='trade',
            unique_together={('sale_offer', 'purchase_offer')},
        ),
    ]
