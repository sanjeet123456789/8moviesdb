# Generated by Django 2.2.3 on 2019-08-07 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Server_name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server_name_id', models.IntegerField()),
                ('server_name', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name_plural': 'server_name',
            },
        ),
    ]