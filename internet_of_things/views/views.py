from internet_of_things.models import Device, DeviceLog, DeviceLogField
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def devices_list(request):
    devices = Device.objects.all()
    context = {"devices": devices}
    return render(request, 'all_devices.html', context=context)

def device_details(request, device_id: int):
    device = Device.objects.get(id=device_id)
    context = {"device": device}
    return render(request, 'device_details.html', context=context)

def device_logs(request, device_id: int):
    logs = DeviceLog.objects.filter(device_id=device_id)
    log_fields = DeviceLogField.objects.filter(device_id=device_id).order_by('sort_order')
    context = {"logs": logs, "log_fields": log_fields}
    return render(request, 'device_logs.html', context=context)