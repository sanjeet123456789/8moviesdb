# Generated by Django 2.2.3 on 2019-08-15 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies_list', '0006_auto_20190815_2327'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movies_list',
            old_name='Awards_id',
            new_name='Award_id',
        ),
    ]
