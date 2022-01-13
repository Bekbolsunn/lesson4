# Generated by Django 4.0.1 on 2022-01-07 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('descriptions', models.TextField(blank=True, null=True)),
                ('is_activate', models.BooleanField()),
                ('duration', models.IntegerField()),
            ],
        ),
    ]