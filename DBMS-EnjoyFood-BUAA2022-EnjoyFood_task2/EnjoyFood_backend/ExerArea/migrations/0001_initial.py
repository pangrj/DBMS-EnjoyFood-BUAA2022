# Generated by Django 4.1 on 2022-12-20 04:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('LifeCircle', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExerArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('l_location', models.CharField(max_length=20)),
                ('l_time', models.CharField(max_length=20)),
                ('l_info', models.CharField(max_length=20)),
                ('lifeCircle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='LifeCircle.lifecircle')),
            ],
        ),
    ]
