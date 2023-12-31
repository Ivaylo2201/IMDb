# Generated by Django 4.2.7 on 2023-12-09 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('imdb_app', '0006_alter_movie_trailer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='imdb_app.director'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='movie',
            name='protagonist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movies', to='imdb_app.actor'),
        ),
    ]
