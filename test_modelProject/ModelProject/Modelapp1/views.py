from django.shortcuts import render
from Modelapp1.models import Grocery_store

def store(request):
    s1=Grocery_store(vegies="Potato", price=20.0)
    s2=Grocery_store(vegies="brinjal", price=25.0)
    s3=Grocery_store(vegies="Tomato", price=30.0)
    s4=Grocery_store(vegies="Carrot", price=35.0)
    s1.save()
    s2.save()
    s3.save()
    s4.save()
    total_veges= Grocery_store.objects.count()
    all_veges= Grocery_store.objects.all()

    return render(request,"Modelapp1/viewTable.html")