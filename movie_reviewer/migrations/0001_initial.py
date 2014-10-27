# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actors',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('actor_first_name', models.CharField(max_length=25)),
                ('actor_last_name', models.CharField(max_length=25)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('movie_title', models.CharField(max_length=100)),
                ('release_date', models.DateField(verbose_name='Date Released')),
                ('director_first_name', models.CharField(max_length=25)),
                ('director_last_name', models.CharField(max_length=25)),
                ('genre', models.CharField(default='action', max_length=25)),
                ('runtime', models.IntegerField(default=0)),
                ('synopsis', models.CharField(max_length=2500)),
                ('avg_score', models.FloatField(editable=False, default=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('movie_rating', models.IntegerField(default=5)),
                ('movie_comments', models.CharField(max_length=2500)),
                ('movie', models.ForeignKey(to='movie_reviewer.Movie')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('user_name', models.CharField(unique=True, max_length=25)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(unique=True, max_length=50)),
                ('user_since', models.DateField(verbose_name='Registration Date')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='review',
            name='reviewer',
            field=models.ForeignKey(to='movie_reviewer.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='actors',
            name='movie',
            field=models.ForeignKey(to='movie_reviewer.Movie'),
            preserve_default=True,
        ),
    ]
