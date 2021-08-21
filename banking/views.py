from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader, RequestContext
from django.db import connection

# Create your views here.

def bank(request):
    template = loader.get_template('banking/bank.html')
    return HttpResponse(template.render())

