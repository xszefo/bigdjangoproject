# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.list import ListView
from . import models
# Create your views here.

class List_Devices(ListView):
	model = models.Device


def list_devices(request):
	context = {}

	return render(request, 'devices/list_devices.html', context)
