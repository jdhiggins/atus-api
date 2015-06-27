__author__ = 'joshuahiggins'
from rest_framework import serializers
from .models import Respondent, HouseholdMember, ActivityCodes, ActivityInstances

class RespondentSerializer(serializers.HyperlinkedModelSerializer):

    household_members = serializers.HyperlinkedIdentityField(view_name='householdmember-list')
    activities = serializers.HyperlinkedIdentityField(view_name='member-activities-list')
    class Meta:
        model = Respondent
        #add fields


class HouseholdMemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HouseholdMember


class ActivityCodesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ActivityCodes


class ActivityInstancesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ActivityInstances

# class ActivityDataSerializer(serializers.HyperlinkedModelSerializer):
#     respondent_count = serializers.IntegerField(read_only=True)
#
#     class Meta:
#         model = ActivityCodes
#         fields =('respondent_count')



