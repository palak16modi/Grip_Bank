from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from django.db import connection
from django.urls import reverse
from django.contrib import messages


def moneytransfer(request):
    cursor = connection.cursor()
    cursor.execute("SELECT ID, CNAME FROM CUSTOMERS;")
    data=cursor.fetchall()
    i=0
    a=[]
    b={}
    while(i<len(data)):
        temp={}
        temp['id']=data[i][0]
        temp['cname']=data[i][1]        
        a.append(temp)
        i+=1
    b['cus']=a
    return render(request,"moneytransfer/cstdetail.html",b)



def onedetail(request):
    userid = request.POST['iidd']
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM CUSTOMERS WHERE ID={};".format(userid))
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
    cursor.execute("SELECT * FROM CUSTOMERS WHERE ID<>{};".format(userid))
    data=cursor.fetchall()
    i=0
    k=[]
    while(i<len(data)):
        temp={}
        temp['id']=data[i][0]
        temp['cname']=data[i][1]   
        temp['cmail']=data[i][2] 
        temp['cur_bal']=data[i][3] 
        temp['city']=data[i][4] 
        k.append(temp)
        i+=1
    b['p']= k
    return render(request,"moneytransfer/onedetail.html",b)
    

def palak(request):
    userid = request.POST.get('cust')
    amt = request.POST.get('amt')
    giver = request.POST.get('giver')
    cursor = connection.cursor()
    cursor.execute("SELECT CUR_BAL FROM CUSTOMERS WHERE ID={};".format(giver))
    data=cursor.fetchall()
    amt=int(amt)
    if(data[0][0]-amt <0):
        b={}
        b['ans']="Amount invalid, please check and try again."
        return render(request,"moneytransfer/messages.html",b)
    else:
        bal=data[0][0]-amt
        cursor.execute("UPDATE CUSTOMERS SET CUR_BAL = {} WHERE ID={};".format(bal,giver))
        cursor.execute("SELECT CUR_BAL FROM CUSTOMERS WHERE ID={};".format(userid))
        data=cursor.fetchall()
        amt=int(amt)
        bal=data[0][0]+amt
        cursor.execute("UPDATE CUSTOMERS SET CUR_BAL = {} WHERE ID={};".format(bal,userid))
        b={}
        b['ans']="Transfer Successful.!"
        
        return render(request,"moneytransfer/messages.html",b)

