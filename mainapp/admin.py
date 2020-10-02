from django.contrib import admin
from mainapp.models import User
from mainapp.models import Project
from mainapp.models import Campaign
from import_export.admin import ImportExportModelAdmin
# Register your models here.

admin.site.register(User)

@admin.register(Project)
class ProjectAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', 'img', 'category', 'author', 'content', 'description', 'funding_target', 'now_funding', 'donator', 'timeline', 'residual_time', 'status', 'url', 'channel', 'days')

@admin.register(Campaign)
class CampaignAdmin(ImportExportModelAdmin):
    list_display = ('id', 'project', 'campaign_img', 'campaign_content', 'campaign_price', 'campaign_people')
