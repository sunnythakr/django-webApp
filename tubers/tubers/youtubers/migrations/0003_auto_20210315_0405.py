# Generated by Django 3.1.7 on 2021-03-14 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0002_auto_20210315_0357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtuber',
            name='its_feature',
            field=models.BooleanField(default=False),
        ),
    ]
