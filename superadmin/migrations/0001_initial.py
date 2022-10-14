# Generated by Django 4.1 on 2022-10-14 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('instituteID', models.AutoField(primary_key=True, serialize=False)),
                ('instituteName', models.TextField(blank=True, max_length=50)),
                ('instituteAddress', models.TextField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('courseID', models.AutoField(primary_key=True, serialize=False)),
                ('courseName', models.TextField(blank=True, max_length=50)),
                ('num_of_semesters', models.TextField(max_length=2)),
                ('instituteName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='institute', to='superadmin.institute')),
            ],
        ),
    ]
