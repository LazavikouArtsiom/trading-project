# Generated by Django 3.1.11 on 2021-05-24 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0006_auto_20210524_1426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='saleoffer',
            name='suitable_offers',
        ),
        migrations.AddField(
            model_name='saleoffer',
            name='suitable_offers',
            field=models.ManyToManyField(blank=True, to='offers.PurchaseOffer'),
        ),
    ]
