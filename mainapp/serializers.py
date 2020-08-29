from django.forms import widgets
from rest_framework import serializers
from . models import Project, campaign

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = campaign
        fields = '__all__'