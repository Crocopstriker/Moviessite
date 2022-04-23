# Generated by Django 4.0.2 on 2022-04-10 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='maleact',
            name='best_movies',
            field=models.CharField(default='The best', max_length=100, verbose_name='Лучшие фильмы'),
        ),
        migrations.AddField(
            model_name='maleact',
            name='biographi',
            field=models.TextField(default='Good or bad actor', max_length=250, verbose_name='Биография'),
        ),
        migrations.AddField(
            model_name='maleact',
            name='title',
            field=models.CharField(default='NONE', max_length=100, verbose_name='Имя'),
        ),
    ]