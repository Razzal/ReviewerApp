# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_reviewer', '0002_auto_20141004_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_image',
            field=models.ImageField(null=True, upload_to='', max_length=2500),
            preserve_default=True,
        ),
    ]
