# Generated by Django 2.2.6 on 2019-10-08 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Entry',
            new_name='Dog',
        ),
    ]