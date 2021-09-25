# Generated by Django 3.2.7 on 2021-09-25 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=35)),
                ('mobile', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=35)),
                ('branch', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
                ('semester', models.IntegerField()),
                ('honors', models.BooleanField(default=False)),
            ],
        ),
    ]
