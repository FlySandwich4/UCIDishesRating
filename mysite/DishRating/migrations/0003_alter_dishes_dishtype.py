# Generated by Django 4.1.5 on 2023-02-04 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DishRating', '0002_dishes_dishcal_dishes_dishrate_dishes_dishtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dishes',
            name='dishType',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
