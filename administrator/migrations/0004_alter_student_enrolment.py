# Generated by Django 4.1 on 2022-10-15 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0003_alter_student_enrolment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='enrolment',
            field=models.BigIntegerField(blank=True),
        ),
    ]
