from django.contrib import admin
from devices import models as dev

# Register your models here.
admin.site.register(dev.DataCenter)
admin.site.register(dev.Rack)
admin.site.register(dev.Vendor)
admin.site.register(dev.Product)
admin.site.register(dev.Device)

