# Generated by Django 4.1.3 on 2022-12-17 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0010_testimonial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='on_display',
            field=models.BooleanField(default=False),
        ),
    ]
