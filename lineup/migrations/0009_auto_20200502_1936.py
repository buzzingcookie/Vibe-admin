# Generated by Django 3.0.5 on 2020-05-02 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lineup', '0008_auto_20200502_1930'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gender',
            old_name='Gender',
            new_name='gender',
        ),
    ]
