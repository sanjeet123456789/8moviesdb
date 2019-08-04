# Generated by Django 2.2.3 on 2019-08-03 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movies_list',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('genres_list_id', models.TextField()),
                ('cast_id', models.TextField()),
                ('director_id', models.PositiveSmallIntegerField()),
                ('writer_id', models.PositiveSmallIntegerField()),
                ('country_id', models.PositiveSmallIntegerField()),
                ('story_line', models.TextField()),
                ('season_id', models.PositiveSmallIntegerField()),
                ('cost', models.IntegerField()),
                ('Awards_id', models.PositiveSmallIntegerField()),
                ('Release', models.DateField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('language_id', models.PositiveSmallIntegerField()),
                ('IMDB_ratting', models.FloatField()),
                ('trailer_link', models.TextField()),
                ('views', models.IntegerField()),
                ('likes', models.TextField()),
                ('ratting', models.FloatField()),
                ('tags', models.TextField()),
            ],
        ),
    ]