# Generated by Django 3.1.5 on 2021-01-19 22:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='item_image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='items',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 19, 23, 23, 6, 978366)),
        ),
    ]
