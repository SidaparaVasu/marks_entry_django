# Generated by Django 4.1 on 2022-10-21 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('superadmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('batchID', models.AutoField(primary_key=True, serialize=False)),
                ('batchName', models.TextField(max_length=50)),
                ('courseName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course1', to='superadmin.course')),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('semesterId', models.AutoField(primary_key=True, serialize=False)),
                ('semester', models.IntegerField()),
                ('courseName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course2', to='superadmin.course')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subjectId', models.AutoField(primary_key=True, serialize=False)),
                ('subject', models.TextField(blank=True, max_length=40)),
                ('credits', models.IntegerField()),
                ('courseName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course3', to='superadmin.course')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='semester1', to='administrator.semester')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrolment', models.BigIntegerField(blank=True)),
                ('seatno', models.TextField(blank=True, max_length=20)),
                ('name', models.TextField(blank=True, max_length=50)),
                ('email', models.EmailField(blank=True, max_length=50)),
                ('phoneno', models.TextField(blank=True, max_length=10)),
                ('gender', models.TextField(blank=True, max_length=6)),
                ('category', models.TextField(blank=True, max_length=10)),
                ('batchName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='batch1', to='administrator.batch')),
                ('courseName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course4', to='superadmin.course')),
                ('instituteName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='institute1', to='superadmin.institute')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='semester2', to='administrator.semester')),
            ],
        ),
    ]
