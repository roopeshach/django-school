# Generated by Django 3.2.5 on 2021-07-16 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20210716_1228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='section',
        ),
    ]