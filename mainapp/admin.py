from django.contrib import admin
from mainapp.models import User
from mainapp.models import Project
from mainapp.models import campaign

admin.site.register(User)
admin.site.register(Project)
admin.site.register(campaign)

# Register your models here.
