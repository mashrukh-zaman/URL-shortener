from django.db import models

# Create your models here.

class UrlData(models.Model):
    url = models.CharField(max_length = 200)
    slug = models.CharField(max_length = 50)
    
    def __str__(self): # why do we need this?
        return f"Short Url for: {self.url} is {self.slug}"