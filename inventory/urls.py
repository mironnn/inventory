from django.conf.urls import patterns, include, url
from django.contrib import admin
from basic.views import index, assets, new_asset, add_new_asset, contact, dict_users, dict_device_type, edit_asset, remove_asset, filter_asset, remove_dict_user, edit_dict_user, new_dict_user, add_new_dict_user, remove_dict_device_type, new_dict_device_type, add_new_dict_device_type, edit_dict_device_type

from django.conf import settings
urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'basic.views.index', name='index'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^index/', 'inventory.views.home', name='index'),
    url(r'^$', index),
    url(r'^index', 'basic.views.index', name='index.html'),
    url(r'^assets', assets),
    # url(r'^write_to_db', write_to_db),
    url(r'^new_asset', new_asset),
    url(r'^add_new_asset', add_new_asset),
    # url(r'^write_to_dictionary', write_to_dict),
    # url(r'^dictionaries', dictionaries),
    url(r'^contact', contact),
    url(r'^dict_users', dict_users),
    url(r'^remove_dict_user', remove_dict_user),
    url(r'^edit_dict_user', edit_dict_user),
    url(r'^new_dict_user', new_dict_user),
    url(r'^add_new_dict_user', add_new_dict_user),
    url(r'^dict_device_type', dict_device_type),
    url(r'^new_dict_device_type', new_dict_device_type),
    url(r'^add_new_dict_device_type', add_new_dict_device_type),
    url(r'^remove_dict_device_type', remove_dict_device_type),
    url(r'^edit_dict_device_type', edit_dict_device_type),
    url(r'^edit_asset', edit_asset),
    url(r'^remove_asset', remove_asset),
    url(r'^filter_asset', filter_asset),
    # url(r'^select_filter_1', select_filter_1),




)
from django.conf.urls.static import static
from basic import views

