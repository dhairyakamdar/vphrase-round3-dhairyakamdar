from django.conf.urls import url
from .views import *
from django.urls import path
from . import views


urlpatterns =[

    url(r'^$', index, name='index'),

    url(r'^display_mobiles$',display_mobiles, name = 'display_mobiles'),

    url(r'^add_mobile$',add_mobile, name = 'add_mobile'),
    

    url(r'^edit_mobile/(?P<pk>\d+)$',edit_mobile,name = 'edit_mobile'),


    url(r'^del_mobile/(?P<pk>\d+)$', del_mobile, name = 'del_mobile'),

   
    # url(r'^search/(?P<pk>\d+)$', search, name = 'search'),

    # path('search/', search, name='search')

    
]
