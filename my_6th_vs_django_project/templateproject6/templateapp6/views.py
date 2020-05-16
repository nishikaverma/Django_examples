from django.shortcuts import render
import datetime

def showdatetime(request):
    d=datetime.datetime.now()
    context={"now":d}
    return render(request,"templateapp6/showdatetime.html",context)


