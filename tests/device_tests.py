from calendar import month

import pytest
from freezegun import freeze_time
from internet_of_things.models import Device, DeviceLog
from datetime import datetime
from dateutil.relativedelta import relativedelta


@pytest.fixture()
def create_devices(db):
    devices = []
    for i in range(3):
        d = Device.objects.create(name=f'Test {i}')
        devices.append(d)
    yield
    for d in devices:
        d.delete()


def test_get_devices(client, create_devices):
    response = client.get('/devices/')
    assert response.status_code == 200
    expected = [
        {'id': 1, 'name': 'Test 0'},
        {'id': 2, 'name': 'Test 1'},
        {'id': 3, 'name': 'Test 2'}
    ]
    data = response.json()
    assert data == expected


def test_get_device(client, create_devices):
    response = client.get('/devices/1')
    assert response.status_code == 200
    expected = {'id': 1, 'name': 'Test 0'}
    data = response.json()
    assert data == expected


@freeze_time('2025-01-01')
def test_post_device_log(client, create_devices):
    payload = {
        "temperature": 2.92,
        "voltage": 0.23,
        "location": "TEST",
        "foo": "bar"
    }
    response = client.post('/devices/log/1', data=payload)
    assert response.status_code == 201
    expected = {'device': 1,
                'id': 1,
                'log': {'foo': 'bar',
                        'location': 'TEST',
                        'temperature': '2.92',
                        'voltage': '0.23'},
                'log_datetime': '2025-01-01T00:00:00Z'}
    data = response.json()
    assert data == expected

expected_device_logs = [{'device': 1,
  'id': 1,
  'log': {'foo': 'bar', 'temperature': 0, 'voltage': 0},
  'log_datetime': '2024-12-01T01:00:00Z'},
 {'device': 1,
  'id': 2,
  'log': {'foo': 'bar', 'temperature': 10, 'voltage': 2},
  'log_datetime': '2025-01-01T01:00:00Z'},
 {'device': 1,
  'id': 3,
  'log': {'foo': 'bar', 'temperature': 20, 'voltage': 4},
  'log_datetime': '2025-02-01T01:00:00Z'},
 {'device': 1,
  'id': 4,
  'log': {'foo': 'bar', 'temperature': 30, 'voltage': 6},
  'log_datetime': '2025-03-01T01:00:00Z'},
 {'device': 1,
  'id': 5,
  'log': {'foo': 'bar', 'temperature': 40, 'voltage': 8},
  'log_datetime': '2025-04-01T01:00:00Z'}]

@freeze_time('2025-01-01 01:00:00')
@pytest.fixture()
def create_device_logs(create_devices):
    for i in range(5):
        d = datetime(2024, 12, 1, 1, 0, 0) + relativedelta(months=i)
        log = {
            'foo': 'bar',
            'temperature': i*10,
            'voltage': i*2
        }
        DeviceLog.objects.create(device_id=1, log=log, log_datetime=d)

@freeze_time('2025-01-01 01:00:00')
@pytest.mark.parametrize('start_date, end_date, expected', [
    (None, None, expected_device_logs),
    ('2025-03-01', None, expected_device_logs[3:]),
    (None, '2025-03-01', expected_device_logs[:3]),
])
def test_get_device_logs_all(client, create_device_logs, start_date, end_date, expected):
    url = '/devices/log/1?'
    if start_date:
        url += f'start_date={start_date}&'
    if end_date:
        url += f'end_date={end_date}'
    response = client.get(url)
    data = response.json()
    assert data == expected
