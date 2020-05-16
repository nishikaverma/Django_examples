from django.shortcuts import render
from django.http import HttpResponse

dict1={'Empno':101,"Ename":"amit","salary":"50000","Hiredate":"Augusth 27,2018"}
dict2={'Empno':102,"Ename":"deepak","salary":"45000","Hiredate":"November 29,2018"}
emp_recs=[dict1,dict2]
context={'emp_list':emp_recs}
def bookview(request):
    
    
    return render(request,'templateapp/showemp.html',context)   

def bookview2(request):
    
    return render(request,'templateapp/showemp2.html',context)