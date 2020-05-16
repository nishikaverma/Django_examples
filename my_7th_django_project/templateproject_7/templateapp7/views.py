from django.shortcuts import render
from datetime import datetime

def ShowDateTimeView(request):
    today=datetime.now()
    context={"now":today}
    return render(request,"templateapp7/showdatetime.html",context)

def homepageViews(request):
    return render(request,"templateapp7/home.html")

def contactpageViews(request):
    return render(request,"templateapp7/contact.html")