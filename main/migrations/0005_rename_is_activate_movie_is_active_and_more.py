# Generated by Django 4.0.1 on 2022-01-14 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_genre_is_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='is_activate',
            new_name='is_active',
        ),
        migrations.AlterField(
            model_name='rating',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='main.movie'),
        ),
    ]
