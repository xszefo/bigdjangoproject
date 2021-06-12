from django.forms import ModelForm, ValidationError
from .models import Device, IpAddressPool
import ipaddress

class CreateDeviceForm(ModelForm):
	class Meta:
		model = Device
		fields = ['name', 'ip_pool', 'ip_address', 'cluster', 'edc_id', 'model']

	def clean(self, *args, **kwargs):
		cleaned_data = super().clean()
		form_name = cleaned_data.get('name')
		form_ip_address = cleaned_data.get('ip_address')
		form_ip_pool = cleaned_data.get('ip_pool')
		form_cluster = cleaned_data.get('cluster')
		
		### Weryfikacja czy adres IP nalezy do odpowiedniej puli
		subnet = form_ip_pool.subnet_object
		ip = ipaddress.IPv4Address(form_ip_address)
		
		if ip not in subnet:
			raise ValidationError('Adres IP musi znajdowac sie w podanej puli')

		### Weryfikacja czy nie duplikuje sie adres IP
		queryset = Device.objects.filter(ip_address=form_ip_address)
		if queryset.count() == 1:
			obj = queryset[0]
			if obj.cluster == True and form_cluster == True:
				return cleaned_data
			elif obj.name == form_name:
				return cleaned_data
			else:
				raise ValidationError('Oba urzadzenia musza byc uczestniczyc w klastrze, aby wspoldzielic IP')
		elif queryset.count() == 2:
			for obj in queryset:
				if obj.name == form_name:
					if form_cluster == True:
						break
					else:
						raise ValidationError('Inne urzadzenie ma juz ten adres IP')
			else:
				raise ValidationError('Zostaly juz skonfigurowane dwa urzadzenia z tym adresem IP')

		return cleaned_data

class UpdateDeviceForm(CreateDeviceForm):
	pass

class CreateIpAddressPool(ModelForm):
	class Meta:
		model = IpAddressPool
		fields = (
			'name',
			'subnet',
			'mask'
		)
	
	# def clean_name(self, *args, **kwargs):
	# 	name = self.cleaned_data.get('name')
	# 	if not IpAddressPool.objects.filter(name=name):
	# 		return name
	# 	raise ValidationError(f'Name {name} is already taken.')

		
	# def clean(self, *args, **kwargs):
	# 	cleaned_data = super().clean(*args, **kwargs)
	# 	name = cleaned_data.get('name')
	# 	subnet = cleaned_data.get('subnet')
	# 	mask = cleaned_data.get('mask')

	# 	print(name, subnet, mask)
	# 	if not IpAddressPool.objects.filter(subnet=subnet, mask=mask):
	# 		return cleaned_data
	# 	raise ValidationError(f'Subnet {subnet}/{mask} already exists.')

class UpdateIpAddressPool(CreateIpAddressPool):
	pass

