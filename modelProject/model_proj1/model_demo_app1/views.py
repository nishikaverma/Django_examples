from django.shortcuts import render
from  model_demo_app1.models import books

def addBooksView(request):
    b1=books(book_id=101, book_name='Let us C', book_price= 450.0 , subject='C', publish_date='2019-05-14')
    b2=books(book_id=102, book_name='Improving Pytho', book_price= 500.0 , subject='Python', publish_date='2019-03-20')
    b3=books(book_id=103, book_name='Python Projects', book_price= 550.0 , subject='Python', publish_date='2019-02-23')
    b1.save() # "save()" for creating the table / saving the contents in DB table
    b2.save()
    b3.save()
    total=books.objects.count()
    context={'count': total}
    return render(request,"model_demo_app1/results.html",context)

def getBooksViews(request):
    all_books=books.objects.all()
    book_list=[]
    for b in all_books:
        book_list.append(b)

    context= {'list_of_Books':book_list}
    return render(request,"model_demo_app1/showBooks.html",context)