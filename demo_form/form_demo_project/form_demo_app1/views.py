from django.shortcuts import render
from form_demo_app1.forms import Contactforms


def contact(request):
    if request.method=='POST':
        form=Contactforms(request.POST)
        if form.is_valid():
            cd =form.cleaned_data
            
            email=cd['email']
            password=cd['password']
            context={'email':email,'password':password}
            return render(request,"form_demo_app1/thankyou.html",context)   
            
    else:
        form=Contactforms()
        return render(request,"form_demo_app1/contact_form.html",{"form":form})


