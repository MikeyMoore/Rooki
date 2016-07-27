from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Notations(models.Model):
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name

class Document(models.Model):
	docfile = models.FileField(upload_to='documents/%Y/%m/%d')


       