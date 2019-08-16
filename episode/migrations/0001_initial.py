# Generated by Django 2.2.3 on 2019-08-15 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('episode_id', models.IntegerField()),
                ('episode_no', models.IntegerField()),
                ('episode_name', models.CharField(max_length=40)),
                ('link_list_id', models.IntegerField()),
                ('episode_duration', models.DurationField()),
                ('views', models.IntegerField(default=0)),
                ('adult', models.BooleanField(default=False)),
                ('filler', models.BooleanField(default=False)),
                ('desc', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'episode',
            },
        ),
    ]