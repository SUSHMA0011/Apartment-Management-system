# Generated by Django 3.2.25 on 2024-08-12 03:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FINALApp', '0049_auto_20240811_2105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaint',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='complaint',
            name='bill_image',
        ),
    ]
