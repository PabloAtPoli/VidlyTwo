# Generated by Django 4.2.5 on 2023-10-27 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0012_alter_movie_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.ForeignKey(default=11, on_delete=django.db.models.deletion.SET_DEFAULT, to='movies.genre'),
        ),
    ]
