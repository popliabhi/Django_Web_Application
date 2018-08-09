# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models

# Create your models here.

class my_blog(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    pub_date=models.DateTimeField(default=datetime.now, blank=True)

    # def __unicode__(self):
    # 	return self.author	