# Generated by Django 4.2.7 on 2025-01-28 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_passedrestaurant_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passedrestaurant',
            name='primary_type_display_name',
            field=models.CharField(choices=[('ramen_restaurant', 'ラーメン屋'), ('fast_food_restaurant', 'ファーストフード'), ('chinese_restaurant', '中華料理'), ('european_restaurant', '欧州料理'), ('japanese_restaurant', '日本料理'), ('izakaya_restaurant', '居酒屋'), ('sushi_restaurant', '寿司屋'), ('meat_restaurant', '肉料理'), ('bakery', 'パン屋'), ('cafe', 'カフェ'), ('bar', 'バー'), ('meal_takeaway', 'テイクアウト')], max_length=255),
        ),
    ]
