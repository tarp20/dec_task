# Generated by Django 3.1.3 on 2020-11-23 21:06

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('Year', models.CharField(blank=True, max_length=25)),
                ('Rated', models.CharField(blank=True, max_length=10)),
                ('Released', models.CharField(blank=True, max_length=25)),
                ('Runtime', models.CharField(blank=True, max_length=25)),
                ('Genre', models.CharField(blank=True, max_length=200)),
                ('Director', models.CharField(blank=True, max_length=100)),
                ('Writer', models.CharField(blank=True, max_length=300)),
                ('Actors', models.CharField(blank=True, max_length=500)),
                ('Plot', models.CharField(blank=True, max_length=900)),
                ('Language', models.CharField(blank=True, max_length=300)),
                ('Country', models.CharField(blank=True, max_length=100)),
                ('Awards', models.CharField(blank=True, max_length=250)),
                ('Poster', models.URLField(blank=True)),
                ('Metascore', models.CharField(blank=True, max_length=5)),
                ('imdbRating', models.CharField(blank=True, max_length=5)),
                ('imdbVotes', models.CharField(blank=True, max_length=100)),
                ('imdbID', models.CharField(blank=True, max_length=100)),
                ('Type', models.CharField(blank=True, max_length=10)),
                ('DVD', models.CharField(blank=True, max_length=25)),
                ('BoxOffice', models.CharField(blank=True, max_length=25)),
                ('Production', models.CharField(blank=True, max_length=100)),
                ('Website', models.CharField(blank=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Source', models.CharField(blank=True, max_length=50)),
                ('Value', models.CharField(blank=True, max_length=20)),
                ('Movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Ratings', to='api_movie.movie')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(blank=True, default=datetime.date.today)),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Comments', to='api_movie.movie')),
            ],
        ),
    ]
