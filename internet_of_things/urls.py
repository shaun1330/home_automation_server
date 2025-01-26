from django.urls import path
from internet_of_things.views import views as htmx_views

app_name = 'iot'

urlpatterns = [
    path('', htmx_views.devices_list, name='devices_list'),  # Render a list of devices
    # path('create/', views.create_device, name='create_device'),  # HTMX form for creating a device
    path('<int:device_id>/', htmx_views.device_details, name='device_detail'),  # Device detail view
]