# Generated by Django 4.2.7 on 2025-01-13 13:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_candidaterestaurant_user_passedrestaurant'),
    ]

    operations = [
        migrations.AddField(
            model_name='passedrestaurant',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='passedrestaurant',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
