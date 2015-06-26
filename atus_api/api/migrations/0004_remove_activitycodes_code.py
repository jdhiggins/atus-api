# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20150626_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activitycodes',
            name='code',
        ),
    ]
