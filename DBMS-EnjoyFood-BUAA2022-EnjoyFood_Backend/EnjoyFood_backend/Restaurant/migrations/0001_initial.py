# Generated by Django 4.1 on 2022-12-24 01:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('LifeCircle', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('re_name', models.CharField(max_length=20)),
                ('re_category', models.CharField(max_length=20)),
                ('re_description', models.CharField(max_length=50)),
                ('lifeCircle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='LifeCircle.lifecircle')),
            ],
        ),
    ]
