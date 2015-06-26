__author__ = 'joshuahiggins'
from rest_framework import serializers
from .models import Respondent, HouseholdMember, ActivityCodes, ActivityInstances

class RespondentSerializer(serializers.HyperlinkedModelSerializer):

    household_members = serializers.HyperlinkedIdentityField(view_name='householdmember-list')
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



