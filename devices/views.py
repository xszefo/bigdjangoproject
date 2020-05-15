# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from . import models
# Create your views here.

class ListDevices(ListView):
	model = models.Device

class CreateDevice(CreateView):
	model = models.Device
	fields = ['name', 'ip_address', 'data_center', 'rack', 'unit', 'model']

