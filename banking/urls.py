from django.conf.urls import url, include
from . import views
from custdetails import views as custdetails_views
from moneytransfer import views as moneytransfer_views
urlpatterns = [
    url(r'banking', views.bank, name="bank"),
    url('custdetails/', custdetails_views.custdetails ,name='custdetails'),
    url(r'^moneytransfer/', include('moneytransfer.urls')),
]