# Generated by Django 4.1.3 on 2022-11-26 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Franchise', '0001_initial'),
        ('account', '0004_remove_employee_center_remove_employee_job_role_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='center',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Franchise.center'),
        ),
        migrations.AddField(
            model_name='employee',
            name='job_role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Franchise.jobrole'),
        ),
    ]
