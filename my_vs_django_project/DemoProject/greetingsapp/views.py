# contains python functions 
# it takes http request and creates output i.e http response 

from django.http import HttpResponse 

def  homepageViews(request):   # it will always take only 1 argument to cereate only 1 http response
    str="<h1> Welcome to Sharma Computer Acadmy ! </h1>"
    return HttpResponse(str)
