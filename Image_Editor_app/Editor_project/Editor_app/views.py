from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return render(request,"Editor_app/homepage.html")

def uploadImg(request):
    #print('The image is here -- on terminal') 
    img=request.GET['ImageUpload']
    context={"UploadedImag":img}
    return render(request,"Editor_app/ImageToEdit.html",context)