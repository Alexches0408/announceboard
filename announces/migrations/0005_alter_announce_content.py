# Generated by Django 4.2.2 on 2023-06-26 07:41

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('announces', '0004_alter_announce_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announce',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
