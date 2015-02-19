from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .forms import Devices, NewDevice, DeviceTypes
from basic.models import device_type, device, user
from django.template.defaulttags import csrf_token

# Create your views here.


def index(request):
    context = {}
    template = "index.html"
    return render(request, template, context)

def assets(request):
    form = Devices()
    devices_all=device.objects.all()
    context = {"form": form, "devices_all": devices_all}
    template = "assets.html"
    return render(request, template, context)

# def new_asset(request):
#     device_types_all=device_type.objects.all()
#     users_all=user.objects.all()
#     context = {"form": form, "device_types_all": device_types_all, "users_all": users_all}
#     template = "new_asset.html"
#     return render(request, template, context)


def new_asset (request):
    form = NewDevice
    users_all=user.objects.all()
    device_type_all=device_type.objects.all()
    context = {"form": form, "users_all": users_all, "device_type_all": device_type_all}
    template = "new_asset.html"

    # nado budet ispolzovat POST
    # new_device = device()
    # if 'device_name' in request.GET:
    #     new_device.device_name = request.GET['device_name']
    # if 'serial_number' in request.GET:
    #     new_device.serial_number = request.GET['serial_number']
    # if 'device_type' in request.GET:
    #     new_device.serial_number = request.GET['device_type']
    # if 'User' in request.GET:
    #     new_device.serial_number = request.GET['User']
    #
    # new_device.save()
    return render(request, template, context)

def add_new_asset (request):
    # if 'add_new_asset' in request.GET:
    new_device = device()
    new_device.device_name = request.GET['new_asset.device.name']
    new_device.User = request.GET['new_asset.device.User']
    new_device.type = request.GET['new_asset.device.type']
    new_device.serial_number = request.GET['new_asset.device.serial_number']
    new_device.date_start = request.GET['new_asset.device.WarrantyStart', False]
    new_device.date_finish = request.GET['new_asset.device.WarrantyEnd', False]
    new_device.save()
        # return HttpResponse('ok')

    return render(request, 'assets.html')

def dictionaries(request):
    context = {}
    template = "dictionaries.html"
    return render(request, template, context)


# def write_to_db (request):
#     if 'device_type_test' in request.GET:
#         type_of_device = device_type()
#         type_of_device.type = request.GET['device_type_test']
#         type_of_device.save()
#         # return HttpResponse('ok')
#     return render(request, 'assets.html')

def write_to_dict (request):
    if 'write_to_dictionary' in request.GET:
        type_of_device = device_type()
        type_of_device.type = request.GET['write_to_dictionary']
        type_of_device.save()
        # return HttpResponse('ok')
    return render(request, 'dictionaries.html')

def generate_devices (request):
    if 'generate_devices' in request.GET:
        my_devices_list = device.objects.all()
        return render_to_response(my_devices_list, 'assets.html')

def generate_devices (request):
    devices_all=device.objects.all()
    return render_to_response('assets.html', {"devices_all": devices_all})


