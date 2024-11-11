# Generated by Django 5.1 on 2024-08-27 15:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('adminapp', '0002_studentlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(choices=[('AOOP', 'Advanced Object-Oriented Programming'), ('PFSD', 'Python Full Stack Development')], max_length=50)),
                ('section', models.CharField(choices=[('S11', 'Section S11'), ('S12', 'Section S12'), ('S13', 'Section S13'), ('S14', 'Section S14'), ('S15', 'Section S15')], max_length=50)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.studentlist')),
            ],
        ),
    ]
