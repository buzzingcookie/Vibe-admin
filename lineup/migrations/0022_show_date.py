# Generated by Django 3.0.5 on 2020-05-02 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lineup', '0021_auto_20200502_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='Date',
            field=models.DateField(null=True),
        ),
    ]
