# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . import models
# Create your views here.

class ListDevices(ListView):
	model = models.Device

class CreateDevice(CreateView):
	model = models.Device
	fields = ['name', 'ip_address', 'data_center', 'model', 'edc_id']

class UpdateDevice(UpdateView):
	model = models.Device
	fields = '__all__'

class DeleteDevice(DeleteView):
	model = models.Device
	success_url = reverse_lazy('devices:list_devices')
