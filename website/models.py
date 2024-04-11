from django.db import models
import datetime
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='media/project_images/', blank=True)
    url = models.URLField(blank=True)
    date = models.DateField()
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Project, self).save(*args,**kwargs)

    def __str__(self):
        return self.name
