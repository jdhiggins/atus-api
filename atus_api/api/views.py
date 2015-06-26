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


class HouseholdMemberListCreateView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = HouseholdMemberSerializer

    def initial(self, request, *args, **kwargs):
        self.respondent = Respondent.objects.get(pk=kwargs['pk'])
        super().initial(request,*args,**kwargs)

    def get_queryset(self):
        return self.respondent.household_members.all()

    def perform_create(self, serializer):
        serializer.save(respondent=self.respondent)
    # def get_queryset(self):
    #     respondentpk = self.kwargs['pk']
    #     return HouseholdMember.objects.filter(respondent__pk=respondentpk)
    #
    # def perform_create(self, serializer):
    #     serializer.save(respondent=self.respondent)


class RespondentActivitiesListCreateView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ActivityInstancesSerializer

    def initial(self, request, *args, **kwargs):
        self.respondent = Respondent.objects.get(pk=kwargs['pk'])
        super().initial(request,*args,**kwargs)

    def get_queryset(self):
        return self.respondent.activity_instances.all()

    def perform_create(self, serializer):
        serializer.save(respondent=self.respondent)



class HouseholdMemberDetailView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = HouseholdMemberSerializer
    queryset = HouseholdMember.objects.all()
    # def get_queryset(self):
    #     return HouseholdMember.objects.get(pk=self.kwargs['pk'])
