# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import django_filters
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . import models
from .forms import CreateDeviceForm, UpdateDeviceForm
# Create your views here.

class DeviceFilter(django_filters.FilterSet):
   class Meta:
        model = models.Device
        fields = {
				'name': ['contains'], 
				'ip_pool': ['exact'], 
				'ip_address': ['contains']
				}

class ListDevices(View):
	def get(self, request):
		dev_filter = DeviceFilter(request.GET, queryset=models.Device.objects.order_by('ip_address', 'name'))
	
		queryset = sorted(dev_filter.qs, key=lambda obj: obj.ip_address_int)
		form = dev_filter.form
		
		context = {
				'queryset': queryset,
				'form': form,
				}
		
	
		return render(request, 'devices/device_list.html', context) 

class CreateDevice(View):
	def get(self, request):
		form = CreateDeviceForm()

		context = {}
		context['form'] = form
		
		return render(request, 'devices/device_form.html', context)

	def post(self, request):
		'''
		Jezeli form przeszedl walidacje, to jest zapisany i nastepuje powrot do listy.
		W innym przypadku strona jest odswiezana z tym samym formularzem, ktory zawiera bledy
		'''
		form = CreateDeviceForm(request.POST)
		if form.is_valid():
			form.save()
			url = reverse_lazy('devices:list_devices')
			return redirect('devices:list_devices')
		else:
			context = {}
			context['form'] = form
			return render(request, 'devices/device_form.html', context)

class UpdateDevice(View):
	def get(self, request, slug):
		instance = models.Device.objects.get(slug=slug)
		form = UpdateDeviceForm(instance=instance)
		context = {}
		context['form'] = form
		
		return render(request, 'devices/device_form.html', context)

	def post(self, request, slug):
		instance = models.Device.objects.get(slug=slug)
		form = UpdateDeviceForm(request.POST, instance=instance)
		if form.is_valid():
			form.save()
			url = reverse_lazy('devices:list_devices')
			return redirect('devices:list_devices')
		else:
			context = {}
			context['form'] = form
			return render(request, 'devices/device_form.html', context)

class DeleteDevice(DeleteView):
	model = models.Device
	success_url = reverse_lazy('devices:list_devices')
