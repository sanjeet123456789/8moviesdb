# Generated by Django 2.2.3 on 2019-08-04 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Award_name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('award_name_id', models.PositiveSmallIntegerField()),
                ('award_name', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name_plural': 'award_name',
            },
        ),
    ]
