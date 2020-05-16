from datetime import *
from django.shortcuts import render
from django.http import HttpResponse


def greet(request):

    return HttpResponse("<b> HELLO ! WELCOME TO THIS PAGE :-) </b></br>")

def currentDate(request):

    d=datetime.now()
    str=d.strftime("%d-%b-%Y")
    browser=request.META['HTTP_USER_AGENT']
    if browser.find("Chrome")!=-1:
        browser="Chrome"
    elif browser.find("Firefox")!=-1:
        browser="Firefox"
    else:
        browser="Unknown browser"
    
    return HttpResponse("<b>Current date  is  "+str+"</b></br>Your browser is "+browser  )

def currentTime(request):

    d=datetime.now()
    str=d.strftime("%I:%M:%S %p")
    return HttpResponse("<b>Current time  is "+str+"</b></br>")

def key_values(request):
    
    return render(request.META,"dateapp/browsers_key.html")

