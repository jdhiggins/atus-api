from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Respondent, HouseholdMember, ActivityCodes, ActivityInstances
from .serializer import RespondentSerializer, HouseholdMemberSerializer, ActivityCodesSerializer, \
    ActivityInstancesSerializer
from rest_framework import viewsets, permissions, generics, filters
from rest_framework.exceptions import PermissionDenied

# Create your views here.
class RespondentViewSet(viewsets.ModelViewSet):
    """Search title, description or long in the style http://localhost:8000/api/bookmarks/?title=mortar"""
    queryset = Respondent.objects.all()
    serializer_class = RespondentSerializer
    permission_classes = (permissions.IsAuthenticated,)
#    filter_backends = (filters.DjangoFilterBackend,)
#    filter_class = RespondentFilter


