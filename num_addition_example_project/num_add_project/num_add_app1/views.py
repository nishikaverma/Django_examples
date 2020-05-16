from django.shortcuts import render
from django.http import HttpResponse

def homePage(request):
    return render(request,"num_add_app1/home.html")

def displayForm(request):
    return render(request,"num_add_app1/show_form.html")


def addnos(request):
    no1=request.GET['num1']
    no2=request.GET['num2']
    sum=int(no1)+int(no2)
    context={'n1':no1,'n2':no2, 'sum':sum}
    return render(request,"num_add_app1/show_result.html",context)
