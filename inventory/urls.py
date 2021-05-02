from django.conf.urls import url
from .views import *


urlpatterns =[

    url(r'^$', index, name='index'),

    url(r'^display_mobiles$',display_mobiles, name = 'display_mobiles'),

    url(r'^add_mobile$',add_mobile, name = 'add_mobile'),
    

    url(r'^edit_mobile/(?P<pk>\d+)$',edit_mobile,name = 'edit_mobile'),


    url(r'^del_mobile/(?P<pk>\d+)$', del_mobile, name = 'del_mobile'),
    

]
