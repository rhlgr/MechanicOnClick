# Generated by Django 4.1.3 on 2022-11-25 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_employee_location_employee_center_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='center',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='job_role',
        ),
        migrations.DeleteModel(
            name='Vehical',
        ),
    ]
