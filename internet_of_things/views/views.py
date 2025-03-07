import django.db.utils
from django.db import transaction
from internet_of_things.models import Device, DeviceLog, DeviceLogField
from django.shortcuts import render, redirect
from internet_of_things.forms import DeviceForm
from django.core.handlers.wsgi import WSGIRequest

def home(request: WSGIRequest):
    print(type(request))
    return render(request, 'home.html')

def devices_list(request: WSGIRequest):
    devices = Device.objects.all()
    context = {"devices": devices}
    return render(request, 'all_devices.html', context=context)

def device_details(request: WSGIRequest, device_id: int):
    device = Device.objects.get(id=device_id)
    context = {"device": device}
    return render(request, 'device_details.html', context=context)

def device_logs(request: WSGIRequest, device_id: int):
    logs = DeviceLog.objects.filter(device_id=device_id)
    log_fields = DeviceLogField.objects.filter(device_id=device_id).order_by('sort_order')
    context = {"logs": logs, "log_fields": log_fields}
    return render(request, 'device_logs.html', context=context)

def create_device(request: WSGIRequest):
    if request.method == 'GET':
        form = DeviceForm()
        return render(request, 'create_device.html', {'form': form})
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            location = form.cleaned_data['location']
            device_type = form.cleaned_data['device_type']
            tags = form.cleaned_data['tags']
            try:
                with transaction.atomic():
                    device = Device.objects.create(name=name, location=location, device_type=device_type)
                    device.save()
                    device.tags.set(tags)
                return redirect('home')
            except django.db.utils.IntegrityError:
                form.add_error('name', 'Device with this name already exists.')
        return render(request, 'create_device.html', {'form': form}, status=400)


