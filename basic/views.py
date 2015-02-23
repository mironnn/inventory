from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from .forms import Devices, NewDevice, DeviceTypes, EditDevice
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
    # print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    # print (request.GET)
    new_device = device()
    new_device.User = user()
    new_device.device_name = request.GET['new_asset.device.name']
    temp_user = request.GET['new_asset.device.User']
    temp_user = str(temp_user)
    # print(temp_user)
    # print(type(temp_user))
    new_device.User = user.objects.get(name=temp_user)
    temp_type = request.GET['new_asset.device.type']
    temp_type = str(temp_type)
    new_device.type = device_type.objects.get(type=temp_type)
    new_device.serial_number = request.GET['new_asset.device.serial_number']
    new_device.date_start = request.GET['new_asset.device.WarrantyStart']
    new_device.date_finish = request.GET['new_asset.device.WarrantyEnd']
    new_device.save()
        # return HttpResponse('ok')

    return (redirect('/assets'))

# def dictionaries(request):
#     context = {}
#     template = "dictionaries.html"
#     return render(request, template, context)


# def write_to_db (request):
#     if 'device_type_test' in request.GET:
#         type_of_device = device_type()
#         type_of_device.type = request.GET['device_type_test']
#         type_of_device.save()
#         # return HttpResponse('ok')
#     return render(request, 'assets.html')

# def write_to_dict (request):
#     if 'write_to_dictionary' in request.GET:
#         type_of_device = device_type()
#         type_of_device.type = request.GET['write_to_dictionary']
#         type_of_device.save()
#         # return HttpResponse('ok')
#     return render(request, 'dictionaries.html')

# def generate_devices (request):
#     if 'generate_devices' in request.GET:
#         my_devices_list = device.objects.all()
#         return render_to_response(my_devices_list, 'assets.html')

def generate_devices (request):
    devices_all=device.objects.all()
    return render_to_response('assets.html', {"devices_all": devices_all})

def contact(request):
    context = {}
    template = "contact.html"
    return render(request, template, context)

def dict_users(request):
    users_all=user.objects.all()
    context = {"users_all": users_all}
    template = "dict_users.html"
    return render(request, template, context)

def remove_dict_user(request):

    user.objects.filter(id = request.GET['remove.ID']).delete()

    return (redirect('/dict_users'))

def edit_dict_user(request):
    if 'edit.ID' in request.GET:
        dict_user_ID = request.GET['edit.ID']
        edited_user = user.objects.get (id = request.GET['edit.ID'])
        User = edited_user.name
        context = {"User": User, "dict_user_ID": dict_user_ID, "edited_user": edited_user}
        template = "edit_dict_users.html"
        return render(request, template, context)

    elif 'edit_dict_user' in request.GET:
        # print('!!!!!!!!!!!!!!!')
        # print(request.GET['edited_dict_user.ID'])
        edited_user = user.objects.get (id = request.GET['edited_dict_user.ID'])
        edited_user.name = request.GET['edit_dict_user.name']
        edited_user.save()

        return (redirect('/dict_users'))
    else:
        return HttpResponse('ok')

def new_dict_user (request):
    context = {}
    template = "new_dict_user.html"
    return render(request, template, context)

def add_new_dict_user (request):
    new_dict_user = user()
    new_dict_user.name = request.GET['add_dict_user.name']
    new_dict_user.save()
    return (redirect('/dict_users'))

def dict_device_type(request):
    context = {}
    template = "dict_device_type.html"
    return render(request, template, context)

def edit_asset(request):
    if 'edit.ID' in request.GET:
        form = EditDevice
        device_ID = request.GET['edit.ID']
        edited_asset = device.objects.get (id = request.GET['edit.ID'])
        # print(edited_asset.type)
        User = edited_asset.User
        type = edited_asset.type
        date_start = edited_asset.date_start
        date_finish = edited_asset.date_finish
        users_all=user.objects.all()
        device_type_all=device_type.objects.all()
        context = {"form": form, "edited_asset": edited_asset, "date_start": date_start, "date_finish": date_finish, "User": User, "type": type, "users_all": users_all, "device_type_all": device_type_all, "device_ID": device_ID}
        template = "edit_asset.html"
        return render(request, template, context)

    elif 'edit_asset' in request.GET:
        device_ID = request.GET['edited_asset.ID']
        print(device_ID)
        edited_asset = device.objects.get (id = request.GET['edited_asset.ID'])
        edited_asset.device_name = request.GET['edit_asset.device.name']
        edited_asset.User = user.objects.get(id=request.GET['edit_asset.device.User'])
        edited_asset.type = device_type.objects.get(pk=request.GET['edit_asset.device.type'])
        edited_asset.serial_number = request.GET['edit_asset.device.serial_number']
        edited_asset.date_start = request.GET['edit_asset.device.WarrantyStart']
        edited_asset.date_finish = request.GET['edit_asset.device.WarrantyEnd']
        edited_asset.save()

        return (redirect('/assets'))
    else:
        return HttpResponse('ok')

def remove_asset(request):

    device.objects.filter(id = request.GET['remove.ID']).delete()

    return (redirect('/assets'))

def filter_asset (request):
    context = {}
    template = "filter_asset.html"
    return render(request, template, context)


