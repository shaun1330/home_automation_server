import pytest



@pytest.fixture
def client():
    from rest_framework.test import APIClient
    return APIClient()


@pytest.fixture
def device_setup(db):
    from internet_of_things.models import Device
    device = Device.objects.create(name='Test Location')
    yield device
    device.delete()