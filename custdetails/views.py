from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from django.db import connection
from django.urls import reverse
from django.contrib import messages


def custdetails(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM CUSTOMERS;")
    data=cursor.fetchall()
    i=0
    a=[]
    b={}
    while(i<len(data)):
        temp={}
        temp['id']=data[i][0]
        temp['cname']=data[i][1]   
        temp['cmail']=data[i][2] 
        temp['cur_bal']=data[i][3] 
        temp['city']=data[i][4]     
        a.append(temp)
        i+=1
    b['cus']=a
    return render(request,"custdetails/custdetails.html",b)



