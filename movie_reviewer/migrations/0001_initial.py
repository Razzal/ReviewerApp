# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
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
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('movie_title', models.CharField(max_length=100)),
                ('release_date', models.DateField(verbose_name='Date Released')),
                ('director_first_name', models.CharField(max_length=25)),
                ('director_last_name', models.CharField(max_length=25)),
                ('genre', models.CharField(default='action', max_length=25)),
                ('runtime', models.PositiveIntegerField(default=0)),
                ('synopsis', models.CharField(max_length=2500)),
                ('avg_score', models.FloatField(editable=False, default=5)),
                ('movie_image', models.ImageField(max_length=2500, null=True, blank=True, upload_to='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NewsArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('article_title', models.CharField(max_length=100)),
                ('article_post_date', models.DateField(verbose_name='Date Posted')),
                ('article_synopsis', models.CharField(max_length=100)),
                ('article_full_text', models.CharField(max_length=20000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('movie_rating', models.IntegerField(default=5)),
                ('movie_comments', models.CharField(max_length=5000)),
                ('movie', models.ForeignKey(to='movie_reviewer.Movie')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReviewUser',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('user_name', models.CharField(max_length=25, unique=True)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('user_since', models.DateField(verbose_name='Registration Date')),
                ('favorite_movie', models.CharField(max_length=50, null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='review',
            name='reviewer',
            field=models.ForeignKey(to='movie_reviewer.ReviewUser'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='newsarticle',
            name='article_poster',
            field=models.ForeignKey(to='movie_reviewer.ReviewUser'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='actor',
            name='movie',
            field=models.ManyToManyField(to='movie_reviewer.Movie'),
            preserve_default=True,
        ),
    ]
