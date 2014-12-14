from django.db import models
import urllib2
import json
# Create your models here.

class consumeRESTAPI(models.Model):
    urlField = models.CharField(max_length=255)
    @property
    def getJSON(self):
        response = urllib2.urlopen(self.urlField)
        data = json.load(response)
        print data
        return data