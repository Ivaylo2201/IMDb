# Generated by Django 4.2.7 on 2023-12-05 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imdb_app', '0005_movie_trailer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='trailer',
            field=models.URLField(),
        ),
    ]
