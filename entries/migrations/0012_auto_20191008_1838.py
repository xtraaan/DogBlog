# Generated by Django 2.2.6 on 2019-10-08 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0011_auto_20191008_1835'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='author',
            new_name='owner',
        ),
    ]