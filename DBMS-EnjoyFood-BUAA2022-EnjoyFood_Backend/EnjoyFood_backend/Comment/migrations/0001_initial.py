# Generated by Django 4.1 on 2022-12-24 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommentPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_star', models.CharField(max_length=20)),
                ('r_content', models.CharField(max_length=100)),
                ('r_data', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
