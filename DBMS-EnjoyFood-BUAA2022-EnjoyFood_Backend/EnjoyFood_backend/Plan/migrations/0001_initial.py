# Generated by Django 4.1 on 2022-12-21 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0006_user_u_avatar'),
        ('Exercise', '0001_initial'),
        ('Dish', '0002_dish_restaurant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=20)),
                ('p_description', models.CharField(max_length=20)),
                ('p_time', models.DateTimeField(auto_now=True)),
                ('calories_in', models.IntegerField(null=True)),
                ('calories_consume', models.IntegerField(null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='User.user')),
            ],
        ),
        migrations.CreateModel(
            name='PlanOfExercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Exercise.exercise')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Plan.plan')),
            ],
        ),
        migrations.CreateModel(
            name='PlanOfDish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dish.dish')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Plan.plan')),
            ],
        ),
    ]
