# Generated by Django 4.2.4 on 2023-08-31 03:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_attendance_reply_alter_attendance_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='attendance',
            field=models.CharField(default='2', max_length=10),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 31, 3, 44, 19, 161758, tzinfo=datetime.timezone.utc)),
        ),
    ]
