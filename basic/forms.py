from django import forms

class Devices (forms.Form):
    field = forms.CharField(max_length=100)


class NewDevice (forms.Form):
    field = forms.CharField(max_length=100)

class DeviceTypes (forms.Form):
    field = forms.CharField(max_length=100)