from django.shortcuts import render
from form_demo_app_1.models import books
from django.http import HttpResponse
def addBooks(request):
    b1=books(book_id=101,book_name='Let us C', book_price=250.0,subject='C',publish_date='2001-01-15')
    b2=books(book_id=102,book_name='Mastering python', book_price=450.0,subject='Python',publish_date='2014-10-21')
    b3=books(book_id=103,book_name='Python projects', book_price=350.0,subject='Python',publish_date='2016-04-09')
    b4=books(book_id=104,book_name='Let us C++', book_price=350.0,subject='C++',publish_date='2006-04-19')
    b5=books(book_id=105,book_name='Mastering C', book_price=340.0,subject='C',publish_date='2014-12-22')
    b6=books(book_id=106,book_name='Learning Java', book_price=650.0,subject='Java',publish_date='2018-11-09')
    b1.save()
    b2.save()
    b3.save()
    b4.save()
    b5.save()
    b6.save()
    total_books=books.objects.count()
    context={"total":total_books}
    return render(request,"form_demo_app_1/addBook_result.html",context)

def search(request):
    
    subj=request.GET['Subject']
    if 'subject' not in request.GET : # when submit is not pressed i.e page is visited 1st time
        return render(request,"form_demo_app_1/search_form.html")
    else: # When submit is pressed & then page is visited
        if subj!="":
            book_list=books.objects.filter(subject__icontains=subj) # to retrive books with subject 'subj' from DB
            context={'subjectName': subj,'books':book_list}
            return render(request,"form_demo_app_1/search_result.html",context)
        else:
            return render(request,"form_demo_app_1/search_form.html",{'error':True})
