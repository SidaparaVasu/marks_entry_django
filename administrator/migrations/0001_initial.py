# Generated by Django 4.1 on 2022-09-24 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('superadmin', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('batchID', models.AutoField(primary_key=True, serialize=False)),
                ('batchName', models.TextField(blank=True, max_length=50)),
                ('courseName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course', to='superadmin.course')),
            ],
        ),
    ]
