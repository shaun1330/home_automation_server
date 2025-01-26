from django.urls import path
from internet_of_things import views


urlpatterns = [
    path('', views.devices_list, name='devices_list'),  # Render a list of devices
    path('create/', views.create_device, name='create_device'),  # HTMX form for creating a device
    path('<int:device_id>/', views.device_detail, name='device_detail'),  # Device detail view
]