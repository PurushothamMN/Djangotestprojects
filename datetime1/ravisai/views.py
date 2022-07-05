from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def datetimeinfo(request):
    date=datetime.datetime.now()
    h=int(date.strftime("%H"))
    msg='<h1> Hello Spark Very '
    if h<12:
        msg=msg+"GM"
    elif h<16:
        msg=msg+"GNoon"
    elif h<21:
        msg=msg+"GE"
    else:
        msg=msg+"GN"
    msg=msg+"</h1><hr>"
    msg=msg+"<h1>Now Server Time is:" +str(date)+'</h1>'
    return HttpResponse(msg)