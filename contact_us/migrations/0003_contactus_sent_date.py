# Generated by Django 3.2.6 on 2021-09-19 15:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0002_remove_contactus_sent_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='sent_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]