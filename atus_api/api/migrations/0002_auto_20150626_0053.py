# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityinstances',
            name='activity',
            field=models.ForeignKey(to='api.ActivityCodes', related_name='activity_instances'),
        ),
        migrations.AlterField(
            model_name='activityinstances',
            name='respondent',
            field=models.ForeignKey(to='api.Respondent', related_name='activity_instances'),
        ),
        migrations.AlterField(
            model_name='householdmember',
            name='respondent',
            field=models.ForeignKey(to='api.Respondent', related_name='household_members'),
        ),
    ]
