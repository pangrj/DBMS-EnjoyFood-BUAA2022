# Generated by Django 4.1.2 on 2022-10-25 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_id', models.IntegerField()),
                ('d_id', models.IntegerField()),
                ('score', models.IntegerField(null=True)),
            ],
        ),
    ]
