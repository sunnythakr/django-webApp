# Generated by Django 3.1.7 on 2021-03-15 08:36

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0008_auto_20210315_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtuber',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
