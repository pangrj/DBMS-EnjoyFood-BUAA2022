# Generated by Django 4.1 on 2022-12-22 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LifeCircle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=20)),
                ('c_location', models.CharField(max_length=20)),
                ('c_description', models.CharField(max_length=20)),
            ],
        ),
    ]
