from django.shortcuts import render
import cx_Oracle

def showbookView(request):
    bookrecords=[]
    errormsg=""
    context={}
    conn=None
    cur=None
    try:
        conn=cx_Oracle.connect("system/oracle123@127.0.0.1/orcl")
        cur=conn.cursor()
        cur.execute("Select book_name,book_price from allbooks")
        booklist=cur.fetchall()
        for name,price in booklist:
            bookrecords.append({"bookname":name,"bookprice":price})
        context['records']=bookrecords
    
    except(cx_Oracle.DatabaseError) as ex :
        errormsg='Some problem in DB'
        print(ex)
        context['error']=errormsg
    
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
        return render(request,"DBapp/showbooks.html",context)
    

    


