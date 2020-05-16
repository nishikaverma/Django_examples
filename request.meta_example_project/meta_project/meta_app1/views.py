from django.shortcuts import render
from django.http import HttpResponse

def display_meta(request):
    
    try:
        browser=request.META['HTTP_USER_AGENT']
        if "Chrome" in browser:
            browser ="Chrome"
        if "Firefox" in browser:
            browser ="Firefox"
    except KeyError:
        browser='unknown browser'
    
    return HttpResponse(f"You are currently using {browser} browser")

def display_all_headders(request):
    headders=request.META
    context={'dict':headders}
    return render(request,"meta_app1/show_headders.html",context)