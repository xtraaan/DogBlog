# Generated by Django 2.2.6 on 2019-10-08 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dog_name', models.CharField(max_length=15)),
                ('breed', models.TextField()),
                ('weight', models.TextField()),
                ('profile_picture', models.ImageField(upload_to='images/profile_pictures/')),
            ],
        ),
    ]