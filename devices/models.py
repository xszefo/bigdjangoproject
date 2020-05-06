# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class DataCenter(models.Model):
	name = models.CharField(max_length=15, null=False, blank=False)
	
class Device(models.Model):
	name = models.CharField(max_length=15, null=False, blank=False)
	ip_address = models.GenericIPAddressField() 

