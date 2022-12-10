# Generated by Django 4.1.3 on 2022-11-25 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_employee_center_remove_employee_job_role_and_more'),
        ('ERP', '0002_alter_providedservice_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='providedservice',
            name='duration',
            field=models.DurationField(),
        ),
        migrations.AlterField(
            model_name='providedservice',
            name='renew_time',
            field=models.DurationField(),
        ),
        migrations.CreateModel(
            name='Vehical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=20)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.customer')),
            ],
        ),
    ]
