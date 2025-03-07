from rest_framework.views import APIView
from internet_of_things.models import Device, DeviceLog
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.request import Request
from internet_of_things.serializer import DeviceSerializer, DeviceLogSerializer

@api_view(['GET'])
def api_get_devices(request: Request):
    devices = Device.objects.all()
    serializer = DeviceSerializer(devices, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_get_device(request: Request, device_id: int):
    device = Device.objects.get(id=device_id)
    serializer = DeviceSerializer(device, many=False)
    return Response(serializer.data)


class DeviceLogAPIView(APIView):
    @staticmethod
    def get(request: Request, device_id: int):
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        device_logs = DeviceLog.objects.filter(device_id=device_id)
        if start_date:
            device_logs = device_logs.filter(log_datetime__gte=start_date)
        if end_date:
            device_logs = device_logs.filter(log_datetime__lte=end_date)
        serializer = DeviceLogSerializer(device_logs, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request: Request, device_id: int):
        print(type(request), "post request type")
        data = request.data
        device_log =  DeviceLog.objects.create(device_id=device_id, log=data)
        serializer = DeviceLogSerializer(device_log, many=False)
        return Response(serializer.data, status=201)


