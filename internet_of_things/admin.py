from django.contrib import admin
from internet_of_things.models import Device, DeviceLog, DeviceLogField, Tags

# Register your models here.

admin.site.register(Device)
admin.site.register(DeviceLog)
admin.site.register(DeviceLogField)
admin.site.register(Tags)
