from django.db import models
from django.utils.timezone import now


class Tags(models.Model):
    name = models.CharField(max_length=255)


class Device(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, default=None, null=True, blank=True)
    device_type = models.CharField(max_length=255, default=None, null=True, blank=True)
    tags = models.ManyToManyField(Tags, default=None, blank=True)


class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    log = models.JSONField()
    log_datetime = models.DateTimeField(default=now)