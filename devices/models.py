# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse
from django.db import models
from django.utils.text import slugify

# Create your models here.

class DataCenter(models.Model):
	name = models.CharField(max_length=15, null=False, blank=False)

	def __str__(self):
		return self.name

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
	cluster = models.BooleanField(default=False)
	data_center = models.ForeignKey(DataCenter, null=True, blank=False, on_delete=models.SET_NULL)
	edc_id = models.PositiveSmallIntegerField(null=False, blank=False, unique=True)
	model = models.ForeignKey(Product, null=True, blank=False, on_delete=models.SET_NULL)
	slug = models.SlugField(unique=True)

	# URL do EDC generowane na podstawie ID urzadzenia
	@property	
	def edc_url(self):
		url = 'http://www.test.pl/{}'.format(self.edc_id)
		return url
	
	# Parametr potrzebny do sortowania listy urzadzen
	@property
	def ip_address_int(self):
		o = [int(octet) for octet in self.ip_address.split('.')]
		res = (16777216 * o[0]) + (65536 * o[1]) + (256 * o[2]) + o[3]
		return res

	# Przy kazdym zapisie obiektu nastepuje przeliczenie SLUG, aby zawsze miec aktualna wartosc na podstawie DC i nazwy
	def save(self, *args, **kwargs):
		temp_slug = '{}-{}'.format(self.data_center.name, self.name)
		self.slug = slugify(temp_slug)
		super(Device, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('devices:list_devices')

	def __str__(self):
		return '{}_{}'.format(self.data_center.name, self.name)

class IpAddressPool(models.Model):
	name = models.CharField(max_length=15, null=False, blank=False)
	subnet = models.GenericIPAddressField()
	mask = models.PositiveSmallIntegerField(null=False, blank=False, default=24)

