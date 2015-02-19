from django.conf.urls import patterns, include, url
from django.contrib import admin
from basic.views import index, assets, dictionaries, write_to_dict, new_asset, add_new_asset

from django.conf import settings
from django.conf.urls.static import static
from basic import views

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
    url(r'^write_to_dictionary', write_to_dict),
    url(r'^dictionaries', dictionaries),

)
