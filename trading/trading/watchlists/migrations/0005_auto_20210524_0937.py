# Generated by Django 3.1.11 on 2021-05-24 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlists', '0004_auto_20210524_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='items',
            field=models.ManyToManyField(blank=True, null=True, related_name='watchlist_item', to='watchlists.WatchlistItem'),
        ),
    ]