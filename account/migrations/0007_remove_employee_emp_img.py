# Generated by Django 4.1.3 on 2023-02-04 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_user_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='emp_img',
        ),
    ]
