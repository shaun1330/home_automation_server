from django.db import models
from django.utils.timezone import now

LOG_DATA_TYPES = [
    ("string", "String"),
    ("int", "Int"),
    ("datetime", "Datetime"),
    ("float", "Float"),
    ("bool", "Bool")
]

class Tags(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Device(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, default=None, null=True, blank=True)
    device_type = models.CharField(max_length=255, default=None, null=True, blank=True)
    tags = models.ManyToManyField(Tags, default=None, blank=True)

    def __str__(self):
        return self.name

class DeviceLogField(models.Model):
    name = models.CharField(max_length=255)
    data_type = models.CharField(choices=LOG_DATA_TYPES, default="string", max_length=50)
    units = models.CharField(max_length=10, null=True, blank=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    sort_order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.device.name} field - {self.name}"

class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    log = models.JSONField()
    log_datetime = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.device.name} log - {self.log_datetime.strftime(format='%Y-%m-%d %H:%M:%S')}"