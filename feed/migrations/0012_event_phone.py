# Generated by Django 3.0.8 on 2021-05-13 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0011_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='phone',
            field=models.IntegerField(default=0),
        ),
    ]
