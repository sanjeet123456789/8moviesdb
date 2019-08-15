# Generated by Django 2.2.3 on 2019-08-15 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writer', '0002_writer_writer_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='writer',
            options={'verbose_name_plural': 'writer'},
        ),
        migrations.RemoveField(
            model_name='writer',
            name='writer_name',
        ),
        migrations.AddField(
            model_name='writer',
            name='writer_name_id',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
