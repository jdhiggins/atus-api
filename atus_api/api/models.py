from django.db import models

# Create your models here.

class Respondent(models.Model):
    id = models.BigIntegerField(primary_key=True)
    # create primary key as well
    final_weight = models.CharField(max_length=255)
    # TUFINLWGT
    age_of_youngest_child = models.CharField(max_length=255)
    # TRYHHCHILD
    age_of_respondent = models.CharField(max_length=255)
    # TEAGE
    sex_of_respondent = models.CharField(max_length=1)
    # TESEX
    # have to convert this one
    highest_education_level = models.CharField(max_length=255)
    # PEEDUCA
    race = models.CharField(max_length=255)
    # PTDTRACE
    is_hispanic = models.CharField(max_length=255)
    # PEHSPNON
    metropolitan_status = models.CharField(max_length=255)
    # GTMETSTA
    labor_force_status = models.CharField(max_length=255)
    # TELFS
    more_than_one_job_in_week = models.CharField(max_length=255)
    # TEMJOT
    full_time_or_part_time = models.CharField(max_length=255)
    # TRDPFTPT
    enrolled_in_school = models.CharField(max_length=255)
    # TESCHENR
    high_school_or_college = models.CharField(max_length=255)
    # TESCHLVL
    spouse_or_partner_present = models.CharField(max_length=255)
    # TRSPPRES
    employment_status_of_spouse_or_partner = models.CharField(max_length=255)
    # TESPEMPNOT
    weekly_earning_at_main_job = models.CharField(max_length=255)
    # TRERNWA
    number_of_children = models.CharField(max_length=255)
    # TRCHILDNUM
    full_time_or_part_time_spouse_partner = models.CharField(max_length=255)
    # TRSPFTPT
    total_hours_worked_per_week = models.CharField(max_length=255)
    # TEHRUSLT
    day_of_week = models.CharField(max_length=255)
    # TUDIARYDAY
    holiday = models.CharField(max_length=255)
    # TRHOLIDAY
    time_spent_on_elder_care = models.CharField(max_length=255)
    # TRTEC
    time_spent_on_secondary_childcare = models.CharField(max_length=255)
    # TRTHH
    #
    # def __str__(self):
    #     return self.id


class HouseholdMember(models.Model):
    respondent = models.ForeignKey(Respondent, related_name="household_members")
    age = models.IntegerField()
    # TEAGE
    sex = models.CharField(max_length=1)
    # TESEX
    relationship_to_respondent = models.CharField(max_length=255)
    # TERRP
    line_number = models.CharField(max_length=255)
    # TULINENO
    # Use TUCASEID TO LINK TO RESPONDENT


class ActivityCodes(models.Model):
    title = models.CharField(max_length=255)


class ActivityInstances(models.Model):
    respondent = models.ForeignKey(Respondent, related_name="activity_instances")
    activity = models.ForeignKey(ActivityCodes, related_name="activity_by_respondent")
    minutes = models.IntegerField()
