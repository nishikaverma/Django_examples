from django.shortcuts import render
from django.http import HttpResponse

def complainFun(request):
    context={'name':"Nishika"}
    return(render(request,"test_app_3/complain.html",context))

