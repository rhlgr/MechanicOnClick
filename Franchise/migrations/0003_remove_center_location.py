# Generated by Django 4.1.3 on 2023-01-28 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Franchise', '0002_location_alter_center_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='center',
            name='location',
        ),
    ]
