from django.shortcuts import render
from django.http import HttpResponse

def Greet(request):
    return HttpResponse("<h3>HELLO EVERYONE ...THIS IS OUR TEST PAGE THROUGH DJANGO ;-) </h3>")

def helpfun(request):
    myname="Nishika  verma"
    return render(request,"test_app_2/help.html",{'name':myname})