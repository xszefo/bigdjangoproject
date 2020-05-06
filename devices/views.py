# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def list_devices(request):
	context = {}

	return render(request, 'devices/list_devices.html', context)
