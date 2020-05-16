from django.shortcuts import render
from CRUD_app1.models import Employee

def home(request):
    return render(request,"CRUD_app1/home.html")

def createit(request):
    return render(request, 'CRUD_app1/create.html')
def create(request): # for inserting a new record
    emp_id=request.GET['e_id']
    name=request.GET['e_name']    
    mail=request.GET['e_mail']
    sal=request.GET['e_sal']
    e1=Employee(e_id=emp_id, e_name=name, e_mail=mail, e_sal=sal)
    e1.save()
    total_rec=Employee.objects.count()
    context={'total':total_rec}
    return render(request,"CRUD_app1/success_create.html",context)

def read(request):# for displaying all records in table
    all_emp=Employee.objects.all()
    context={'emp_list':all_emp}
    return render(request,"CRUD_app1/read.html",context)

def updateit(request):
    return render(request, 'CRUD_app1/update_form_entry.html')
def searchDetails(request):
    return render(request, 'CRUD_app1/update_form_result.html')
def update(request): # for updating the records in table
    u_id=request.GET['e_id']
    emp_list=Employee.objects.filter(e_id=u_id).update(e_name=request.GET['e_name'],e_mail=request.GET['e_mail'] , e_sal=request.GET['e_sal'])
    context={'record':emp_list}
    return render(request,"CRUD_app1/success_update.html",context)

def deleteall(request): #for deleting all a records
    Employee.objects.all().delete()
    return render(request,"CRUD_app1/all_delete_msg.html")
def deleteit(request):
    return render(request, 'CRUD_app1/delete_entry.html')
def deleteone(request):# for deleting a record
    emp_id=request.GET['e_id']
    Employee.objects.filter(e_id=emp_id).delete()
    return render(request,"CRUD_app1/all_delete_msg")        
