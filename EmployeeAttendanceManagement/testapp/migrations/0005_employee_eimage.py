# Generated by Django 2.1.11 on 2019-10-10 21:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0004_remove_employee_eimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='eimage',
            field=models.ImageField(default=datetime.datetime(2019, 10, 10, 21, 3, 38, 515730, tzinfo=utc), upload_to='images/'),
            preserve_default=False,
        ),
    ]
