from django.urls import path
from .views import *
from banking import views as banking_views
from . import views
from django.conf.urls import url

urlpatterns = [
    url('custdetails', custdetails ,name='custdetails'),
    path('transfer', views.onedetails, name="onedetails"),
    path('palak', views.palak, name="palak" ),
    path('back', banking_views.bank, name="back"),
    path('', views.moneytransfer, name='moneytransfer'),
]
