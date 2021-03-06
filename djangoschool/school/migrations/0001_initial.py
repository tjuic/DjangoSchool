# Generated by Django 4.0 on 2022-01-09 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(choices=[('Math', 'Math'), ('Science', 'Science'), ('Computer', 'Computer'), ('Physical Edu', 'Physical Edu'), ('Art', 'Art'), ('Physics', 'Physics'), ('Biology', 'Biology'), ('English', 'English')], default='Math', max_length=200)),
                ('student_name', models.CharField(max_length=200)),
                ('score', models.IntegerField(default=0)),
            ],
        ),
    ]
