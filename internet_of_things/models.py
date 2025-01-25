from django.db import models
from django.utils.timezone import now


class Device(models.Model):
    name = models.CharField(max_length=255)


class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    log = models.JSONField()
    log_datetime = models.DateTimeField(default=now)