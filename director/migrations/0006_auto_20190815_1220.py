# Generated by Django 2.2.3 on 2019-08-15 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('director', '0005_director_director_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='director',
            name='director_name',
        ),
        migrations.RemoveField(
            model_name='director',
            name='image_id',
        ),
        migrations.AddField(
            model_name='director',
            name='director_name_id',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
