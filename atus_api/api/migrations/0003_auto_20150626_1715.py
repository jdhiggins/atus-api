# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20150626_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitycodes',
            name='code',
            field=models.CharField(max_length=7),
        ),
        migrations.AlterField(
            model_name='activityinstances',
            name='activity',
            field=models.ForeignKey(to='api.ActivityCodes', related_name='activity_by_respondent'),
        ),
    ]
