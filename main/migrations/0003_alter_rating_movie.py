# Generated by Django 4.0.1 on 2022-01-12 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_genre_alter_movie_name_rating_movie_genres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating', to='main.movie'),
        ),
    ]
