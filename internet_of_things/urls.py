from django.urls import path
from internet_of_things import views

urlpatterns = [
    path('', views.get_devices),
    path('<int:device_id>', views.get_device),
    path('log/<int:device_id>', views.DeviceLogView.as_view()),
]