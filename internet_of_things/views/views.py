from internet_of_things.models import Device, DeviceLog
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
