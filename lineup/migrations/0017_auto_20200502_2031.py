# Generated by Django 3.0.5 on 2020-05-02 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lineup', '0016_auto_20200502_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='EventAV',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
