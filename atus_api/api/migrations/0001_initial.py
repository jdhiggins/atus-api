# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityCodes',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('code', models.IntegerField()),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ActivityInstances',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('minutes', models.IntegerField()),
                ('activity', models.ForeignKey(to='api.ActivityCodes')),
            ],
        ),
        migrations.CreateModel(
            name='HouseholdMember',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(max_length=1)),
                ('relationship_to_respondent', models.IntegerField()),
                ('line_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Respondent',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('final_weight', models.DecimalField(max_digits=20, decimal_places=6)),
                ('age_of_youngest_child', models.IntegerField()),
                ('age_of_respondent', models.IntegerField()),
                ('sex_of_respondent', models.CharField(max_length=1)),
                ('highest_education_level', models.IntegerField()),
                ('race', models.IntegerField()),
                ('is_hispanic', models.IntegerField()),
                ('metropolitan_status', models.IntegerField()),
                ('labor_force_status', models.IntegerField()),
                ('more_than_one_job_in_week', models.IntegerField()),
                ('full_time_or_part_time', models.IntegerField()),
                ('enrolled_in_school', models.IntegerField()),
                ('high_school_or_college', models.IntegerField()),
                ('spouse_or_partner_present', models.IntegerField()),
                ('employment_status_of_spouse_or_partner', models.IntegerField()),
                ('weekly_earning_at_main_job', models.IntegerField()),
                ('number_of_children', models.IntegerField()),
                ('full_time_or_part_time_spouse_partner', models.IntegerField()),
                ('total_hours_worked_per_week', models.IntegerField()),
                ('day_of_week', models.IntegerField()),
                ('holiday', models.IntegerField()),
                ('time_spent_on_elder_care', models.IntegerField()),
                ('time_spent_on_secondary_childcare', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='householdmember',
            name='respondent',
            field=models.ForeignKey(to='api.Respondent'),
        ),
        migrations.AddField(
            model_name='activityinstances',
            name='respondent',
            field=models.ForeignKey(to='api.Respondent'),
        ),
    ]
