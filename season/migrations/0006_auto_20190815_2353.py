# Generated by Django 2.2.3 on 2019-08-15 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('season', '0005_auto_20190815_2327'),
    ]

    operations = [
        migrations.RenameField(
            model_name='season',
            old_name='eposide_id',
            new_name='episode_id',
        ),
    ]
