# Generated by Django 3.2.5 on 2021-08-01 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=60)),
                ('faculty_name', models.CharField(max_length=200)),
                ('nos', models.IntegerField(default=20)),
            ],
        ),
    ]