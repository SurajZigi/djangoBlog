# Generated by Django 3.0.2 on 2020-01-12 20:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200103_0237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_psoted',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 12, 20, 46, 59, 398762, tzinfo=utc)),
        ),
    ]
