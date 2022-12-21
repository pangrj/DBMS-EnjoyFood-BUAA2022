# Generated by Django 4.1 on 2022-12-21 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0006_user_u_avatar'),
        ('Plan', '0001_initial'),
        ('Comment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentplan',
            name='plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Plan.plan'),
        ),
        migrations.AddField(
            model_name='commentplan',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.user'),
        ),
    ]
