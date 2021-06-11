from django.contrib import admin
from devices import models as dev
from core import models as core

# Register your models here.
admin.site.register(dev.Vendor)
admin.site.register(dev.Product)
admin.site.register(dev.Device)
admin.site.register(dev.IpAddressPool)
admin.site.register(core.User)
