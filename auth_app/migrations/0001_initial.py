# Generated by Django 4.1 on 2022-09-24 12:47

import auth_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminname', models.TextField(max_length=20)),
                ('adminpassword', models.TextField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=50)),
                ('phoneno', models.TextField(max_length=10)),
                ('password', models.TextField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to=auth_app.models.filepath)),
                ('type', models.IntegerField()),
            ],
        ),
    ]
