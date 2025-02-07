from django import forms
from internet_of_things.models import Tags


from django import forms
from internet_of_things.models import Tags

class DeviceForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter device name',
            'id': 'deviceName'
        })
    )
    location = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter location',
            'id': 'deviceLocation'
        })
    )
    device_type = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter device type',
            'id': 'deviceType'
        })
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tags.objects.all(),
        to_field_name="id",
        widget=forms.SelectMultiple(attrs={
            'class': 'form-control',
            'id': 'deviceTags'
        }),
        required=False,
    )