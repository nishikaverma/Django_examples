from django.shortcuts import render
from book_app1.models import books

def homePageviews(request):
    return render(request,"book_app1/home.html")

def takeBooksrecord(request):
    return render(request,"book_app1/take_books_record.html")

def addBooksToDB(request):
    
    b_id=request.GET['bookid']
    b_name=request.GET['bookname']
    b_date=request.GET['Publishdate']
    b_subject=request.GET['booksubject']
    b_price=request.GET['bookprice']
    book_list=[b_id,b_name,b_price,b_subject,b_date]
    context={'record':book_list, 'book_name':b_name}
    b=books(book_id=b_id , book_name=b_name , book_price=b_price, subject=b_subject ,publish_date=b_date)
    b.save()
    return render(request,"book_app1/add_books_to_DB.html",context)



def showBooks(request):
    records=books.objects.all() # where records is the list of names of all the books present in db table books
    context={'book_records':records}
    return render(request,"book_app1/show_books.html",context)
