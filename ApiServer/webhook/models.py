from django.db import models

# Create your models here.
class Log(models.Model):
    pub_date = models.DateTimeField('date published', auto_now=True)
    json_data = models.TextField()
