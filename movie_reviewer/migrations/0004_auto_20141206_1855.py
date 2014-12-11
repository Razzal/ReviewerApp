# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_reviewer', '0003_auto_20141130_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_image',
            field=models.FileField(upload_to='', max_length=2500, blank=True, null=True),
            preserve_default=True,
        ),
    ]
