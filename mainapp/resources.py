from import_export import resources
from .models import Project, Campaign
# from import_export.widgets import ForeignKeyWidget
from import_export import resources, widgets, fields

class ProjectResource(resources.ModelResource):
    class Meta:
        model = Project
class CampaignResource(resources.ModelResource):
    # class Meta:
    #     model = campaign
    project = fields.Field(
        column_name='project',
        attribute='project',
        widget=widgets.ForeignKeyWidget(Project, 'id'))
    class Meta:
        fields = ('id', 'project', 'campaign_img', 'campaign_content', 'campaign_price', 'campaign_people')
        model = Campaign