# Generated by Django 4.1.3 on 2023-01-10 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_user_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='facbook_link',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='insta_link',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='job_role',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='on_emp_display',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='on_tech_display',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='store',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='twitter_link',
        ),
    ]
