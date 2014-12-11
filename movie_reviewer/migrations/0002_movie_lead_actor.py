# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_reviewer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='lead_actor',
            field=models.CharField(blank=True, null=True, max_length=50),
            preserve_default=True,
        ),
    ]
