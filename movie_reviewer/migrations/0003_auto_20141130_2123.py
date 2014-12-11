# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('movie_reviewer', '0002_movie_lead_actor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsarticle',
            options={'ordering': ['-article_post_date']},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-review_post_date']},
        ),
        migrations.AddField(
            model_name='review',
            name='review_post_date',
            field=models.DateField(default=datetime.date(2014, 11, 30), verbose_name='Date Posted'),
            preserve_default=False,
        ),
    ]
