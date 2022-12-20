# Generated by Django 4.1 on 2022-12-20 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sp_name', models.CharField(max_length=20)),
                ('sp_content', models.CharField(max_length=20)),
                ('sp_difficulty', models.CharField(max_length=20)),
                ('sp_calories', models.IntegerField()),
                ('sp_time', models.IntegerField()),
            ],
        ),
    ]
