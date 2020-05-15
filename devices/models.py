# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse
from django.db import models

# Create your models here.

class DataCenter(models.Model):
	name = models.CharField(max_length=15, null=False, blank=False)

	def __str__(self):
		return self.name

class Rack(models.Model):
	name = models.CharField(max_length=15, null=False, blank=False)
	data_center = models.ForeignKey(DataCenter, null=True, blank=False, on_delete=models.SET_NULL)

	def __str__(self):
		return '{}'.format(self.name)

class Vendor(models.Model):
	name = models.CharField(max_length=15, null=False, blank=False)

	def __str__(self):
		return self.name

class Product(models.Model):
	name = models.CharField(max_length=30, null=False, blank=False)
	vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)

	def __str__(self):
		return '{} {}'.format(self.vendor, self.name)

class Device(models.Model):
	name = models.CharField(max_length=15, null=False, blank=False, unique=True)
	ip_address = models.GenericIPAddressField() 
	data_center = models.ForeignKey(DataCenter, null=True, blank=False, on_delete=models.SET_NULL)
	rack = models.ForeignKey(Rack, null=True, blank=True, on_delete=models.SET_NULL)
	unit = models.CharField(max_length=2, null=True, blank=True)
	model = models.ForeignKey(Product, null=True, blank=False, on_delete=models.SET_NULL)

	def get_absolute_url(self):
		return reverse('devices:list_devices')

	def __str__(self):
		return '{}_{}'.format(self.data_center.name, self.name)

class IpAddressPool(models.Model):
	name = models.CharField(max_length=15, null=False, blank=False)
	subnet = models.GenericIPAddressField()
	mask = models.PositiveSmallIntegerField(null=False, blank=False, default=24)
