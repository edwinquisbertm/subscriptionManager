# Generated by Django 5.1.4 on 2024-12-14 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='duration',
        ),
    ]
