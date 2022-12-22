# Generated by Django 4.1.3 on 2022-12-22 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_alter_employee_emp_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='on_display',
            new_name='on_tech_display',
        ),
        migrations.AddField(
            model_name='employee',
            name='on_emp_display',
            field=models.BooleanField(default=False),
        ),
    ]
