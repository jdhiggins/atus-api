"""atus_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""


from django.conf.urls import include, url
from django.contrib import admin

from api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'respondents', views.RespondentViewSet, base_name='respondent')
router.register(r'activity-codes', views.ActivitiesViewSet)


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
    url(r'^respondents/(?P<pk>\d+)/household-members/$', views.HouseholdMemberListCreateView.as_view(),
        name="householdmember-list"),
    url(r'^household-members/(?P<pk>\d+)/$', views.HouseholdMemberDetailView.as_view(),
        name="householdmember-detail"),
    url(r'^respondents/(?P<pk>\d+)/activity-codes/$', views.RespondentActivitiesListCreateView.as_view(),
        name='member-activities-list'),
    url(r'^activity-instance/(?P<pk>\d+)/$', views.ActivityInstanceDetailView.as_view(),
        name="activityinstances-detail"),
    url(r'^activity-instance-data/(?P<pk>\d+)/$', views.ActivitiesDataView.as_view(),
        name="activity-data-detail"),
]
