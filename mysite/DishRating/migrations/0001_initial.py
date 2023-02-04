# Generated by Django 4.1.5 on 2023-02-04 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dishes',
            fields=[
                ('dishName', models.CharField(max_length=30)),
                ('dishID', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('userName', models.CharField(max_length=10)),
                ('userAccount', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('userPassword', models.CharField(max_length=30)),
                ('userSignupDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=150)),
                ('pubDate', models.DateTimeField()),
                ('dishID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DishRating.dishes')),
                ('userAccount', models.ForeignKey(on_delete=models.SET('User Deleted the Account'), to='DishRating.users')),
            ],
        ),
    ]
