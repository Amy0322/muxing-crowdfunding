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
    id = models.IntegerField(null=False,primary_key=True)
    title = models.CharField(max_length=128, null=False)
    img = models.URLField(null=False)
    category = models.CharField(max_length=8, null=False)
    author = models.CharField(max_length=64, null=False)
    content = models.TextField()
    description = models.TextField(null=False)
    funding_target = models.IntegerField(null=False)
    now_funding = models.IntegerField(null=False)
    donator = models.IntegerField(null=False)
    timeline = models.CharField(max_length=64,null=False)
    residual_time = models.CharField(max_length=16,null=False)
    status = models.CharField(max_length=8)
    url = models.URLField(null=False)
    channel = models.CharField(max_length=8, null=False, default="unknown")
    days = models.IntegerField(null=False, default=0)

    def __str__(self):
        return "%s %s" % (self.id, self.title)


class Campaign(models.Model):
    id = models.IntegerField(null=False, primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    campaign_img = models.URLField()
    campaign_content = models.TextField()
    campaign_price = models.IntegerField()
    campaign_people = models.IntegerField()

    def __str__(self):
        return "%s %s" % (self.id, self.project)

