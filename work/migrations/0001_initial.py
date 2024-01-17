# Generated by Django 5.0.1 on 2024-01-17 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=200)),
                ('img', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('short_desc', models.CharField(max_length=200)),
                ('long_desc', models.CharField(max_length=200)),
                ('tags', models.CharField(max_length=200)),
            ],
        ),
    ]