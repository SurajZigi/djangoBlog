# Generated by Django 3.0.2 on 2020-01-13 11:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200113_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_psoted',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 13, 11, 42, 28, 792526, tzinfo=utc)),
        ),
    ]
