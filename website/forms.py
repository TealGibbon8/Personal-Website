from django import forms
from website.models import *
from django.contrib.auth.models import User

class ProjectForm(forms.ModelForm):
    name = forms.CharField(max_length=255)
    description = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField(required=False)
    url = forms.URLField(required=False, help_text="Please enter the URL of the project if there is one.")
    date = forms.DateField(required=False,widget=forms.SelectDateWidget())
    slug = forms.CharField(widget=forms.HiddenInput(),required=False)
    class Meta:
        model = Project
        fields = ['name', 'description', 'image', 'url', 'date']