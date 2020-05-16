from django.shortcuts import render
from django.http import HttpRequest
def homepageviews(request):
    name="Nishika"
    city="Bhopal"
    context={"myname":name , "mycity":city}
    return render(request,"template_app/index.html", context)

