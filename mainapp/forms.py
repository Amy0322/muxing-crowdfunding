from django.forms import ModelForm
from .models import Project


class MyForm(ModelForm):
    class Meta:
        model = Project
        fields = ('title','description')
    # exclude = 'firstname'