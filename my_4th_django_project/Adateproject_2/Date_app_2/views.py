from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
def show_date(request):
    d=datetime.now()
    context={"date":d}
    return render(request,"Date_app_2/date.html",context)


