# Generated by Django 2.1.11 on 2019-10-10 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0005_employee_eimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='eimage',
        ),
    ]
