# Generated by Django 2.2.6 on 2019-10-04 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0003_auto_20191004_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='entry_image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]