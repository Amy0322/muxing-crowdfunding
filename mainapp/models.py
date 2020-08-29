from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class User(models.Model):
    proj_name = models.CharField(max_length=64,null=False)
    proj_type = models.CharField(max_length=16,null=False)
    proj_funding_target = models.IntegerField(null=False)
    proj_duration = models.IntegerField(null=False)
    proj_campaign_num = models.IntegerField(null=False)
    proj_description = models.TextField(null=False)
    proj_add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.proj_name

class Project(models.Model):
    project_id = models.IntegerField(null=False,primary_key=True)
    title = models.CharField(max_length=128, null=False)
    category = models.CharField(max_length=8, null=False)
    content = models.TextField()
    description = models.TextField(null=False)
    author = models.CharField(max_length=64,null=False)
    now_funding = models.IntegerField(null=False)
    funding_target = models.IntegerField(null=False)
    donator = models.IntegerField(null=False)
    timeline = models.CharField(max_length=64,null=False)
    residual_time = models.IntegerField(null=False)
    status = models.CharField(max_length=8)
    url = models.URLField(null=False)
    img = models.URLField(null=False)

    def __str__(self):
        return self.title


class campaign(models.Model):
    project_id = models.ForeignKey('Project', blank=True, null=True)
    campaign_img = models.URLField()
    campaign_content = models.TextField()
    campaign_price = models.IntegerField()
    campaign_people = models.IntegerField()

