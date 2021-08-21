from django.urls import path
from .views import *
from banking import views as banking_views
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.moneytransfer, name='moneytransfer'),
    path('transfer', views.onedetail, name="onedetail"),
    path('palak', views.palak, name="palak" ),
    path('back', banking_views.bank, name="back"),
]
