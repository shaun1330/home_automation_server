from internet_of_things.models import Device, DeviceLog, DeviceLogField, Tags
import json
import datetime

def test_device_str(db):
    device = Device.objects.create(name="Test")
    expected = "Test"
    output = str(device)
    assert expected == output

def test_device_log_field_str(db):
    device = Device.objects.create(name="Test")
    log_field = DeviceLogField.objects.create(name="TestField", device=device)
    expected = "Test field - TestField"
    output = str(log_field)
    assert expected == output

def test_device_log_str(db):
    device = Device.objects.create(name="Test")
    payload = json.dumps({"hello": "world"})
    d = datetime.datetime(2025, 1, 1, 0, 0, 0)
    log = DeviceLog.objects.create(device=device, log_datetime=d, log=payload)
    expected = "Test log - 2025-01-01 00:00:00"
    output = str(log)
    assert expected == output

def test_tag_str(db):
    tags = Tags.objects.create(name="TestTag")
    expected = "TestTag"
    output = str(tags)
    assert expected == output
