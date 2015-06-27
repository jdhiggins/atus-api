from django.db import models

# Create your models here.

class Respondent(models.Model):
    #create primary key as well
    final_weight = models.CharField(max_length=255)
    #TUFINLWGT
    age_of_youngest_child = models.IntegerField()
    #TRYHHCHILD
    age_of_respondent = models.IntegerField()
    #TEAGE
    sex_of_respondent = models.CharField(max_length=1)
    #TESEX
    #have to convert this one
    highest_education_level = models.IntegerField()
    #PEEDUCA
    race = models.IntegerField()
    #PTDTRACE
    is_hispanic = models.IntegerField()
    #PEHSPNON
    metropolitan_status = models.IntegerField()
    #GTMETSTA
    labor_force_status = models.IntegerField()
    #TELFS
    more_than_one_job_in_week = models.IntegerField()
    #TEMJOT
    full_time_or_part_time = models.IntegerField()
    #TRDPFTPT
    enrolled_in_school = models.IntegerField()
    #TESCHENR
    high_school_or_college = models.IntegerField()
    #TESCHLVL
    spouse_or_partner_present = models.IntegerField()
    #TRSPPRES
    employment_status_of_spouse_or_partner = models.IntegerField()
    #TESPEMPNOT
    weekly_earning_at_main_job = models.IntegerField()
    #TRERNWA
    number_of_children = models.IntegerField()
    #TRCHILDNUM
    full_time_or_part_time_spouse_partner = models.IntegerField()
    #TRSPFTPT
    total_hours_worked_per_week = models.IntegerField()
    #TEHRUSLT
    day_of_week = models.IntegerField()
    #TUDIARYDAY
    holiday = models.IntegerField()
    #TRHOLIDAY
    time_spent_on_elder_care = models.IntegerField()
    #TRTEC
    time_spent_on_secondary_childcare = models.IntegerField()
    #TRTHH
    #
    # def __str__(self):
    #     return self.id

class HouseholdMember(models.Model):
    respondent = models.ForeignKey(Respondent, related_name="household_members")
    age = models.IntegerField()
    #TEAGE
    sex = models.CharField(max_length=1)
    #TESEX
    relationship_to_respondent = models.IntegerField()
    #TERRP
    line_number = models.IntegerField()
    #TULINENO
    #Use TUCASEID TO LINK TO RESPONDENT


class ActivityCodes(models.Model):
    title = models.CharField(max_length=255)
    

class ActivityInstances(models.Model):
    respondent = models.ForeignKey(Respondent, related_name="activity_instances")
    activity = models.ForeignKey(ActivityCodes, related_name="activity_by_respondent")
    minutes = models.CharField(max_length=255)

