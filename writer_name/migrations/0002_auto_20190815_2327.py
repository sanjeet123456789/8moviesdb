# Generated by Django 2.2.3 on 2019-08-15 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writer_name', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='writer_name',
            name='writer_name',
            field=models.CharField(default=0, max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='writer_name',
            name='image_id',
            field=models.IntegerField(default=1),
        ),
    ]
