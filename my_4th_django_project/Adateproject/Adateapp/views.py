from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
def showdate(request):
    d=datetime.now()
    str=d.strftime("%d-%b-%Y")
    context= {"date":str}
    return render(request,"Adateapp/index.html",context)
