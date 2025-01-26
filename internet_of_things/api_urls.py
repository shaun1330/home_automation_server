from django.urls import path
from internet_of_things.views import api_views

urlpatterns = [
    path('', api_views.api_get_devices),
    path('<int:device_id>', api_views.api_get_device),
    path('log/<int:device_id>', api_views.DeviceLogAPIView.as_view()),
]