# Generated by Django 4.2.1 on 2023-11-09 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='pho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
            ],
        ),
    ]
