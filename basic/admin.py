from django.contrib import admin

# Register your models here.

from basic.models import user, device, device_type

admin.site.register (device)
admin.site.register (user)
admin.site.register (device_type)