# Generated by Django 4.1.3 on 2022-12-17 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_employee_facbook_link_employee_insta_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_img',
            field=models.ImageField(default='media/empimg/AviDP.jpeg', upload_to='media/empimg'),
        ),
    ]
