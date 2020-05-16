from django.shortcuts import render
from django_form_app1.forms import Contactforms

def contact(request):
    if request.method=='POST':
        form=Contactforms(request.POST)
        if form.is_valid():
            cd =form.cleaned_data
            subj=cd['subject']
            email=cd['email']
            msg=cd['msg']
            context={"subject":subj,'email':email,'message':msg}
            return render(request,"django_form_app1/thankyou.html",context)   
            
    else:
        form=Contactforms()
        return render(request,"django_form_app1/contact_form.html",{"form":form})
