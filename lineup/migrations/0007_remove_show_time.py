# Generated by Django 3.0.5 on 2020-05-01 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lineup', '0006_auto_20200501_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='show',
            name='Time',
        ),
    ]
