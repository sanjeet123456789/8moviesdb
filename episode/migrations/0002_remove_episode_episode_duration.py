# Generated by Django 2.2.3 on 2019-08-15 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('episode', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='episode',
            name='episode_duration',
        ),
    ]