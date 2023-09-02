from django.shortcuts import render , redirect
from app1.models import Employee


def Index(request):
    employee = Employee.objects.all()
    emp={
        'emp':employee
    }
    return render(request,"index.html",emp)

def add(request):
    if(request.method=="POST"):
        Name = request.POST.get('Name')
        Email = request.POST.get('Email')
        Address = request.POST.get('Address')
        Phone = request.POST.get('Phone')
        emp = Employee(
            Name = Name,
            Email = Email,
            Address = Address,
            Phone = Phone
            )
        emp.save()
        return redirect('index')
    
    return render(request,"Index.html")


def edit(request):
    employee = Employee.objects.all()
    emp={
        'emp':employee
    }
    return render(request,"Index.html",emp)

def Update(request,id):
    if request.method == "POST":
        Name = request.POST.get("Name")
        Email = request.POST.get("Email")
        Address = request.POST.get("Address")
        Phone = request.POST.get("Phone")
        emp = Employee(
            id = id,
            Name = Name,
            Email =Email,
            Address = Address,
            Phone = Phone
        )
        emp.save()
        return redirect('index')
    return render(request, "Index.html")

def Delete(request,id):
    emp = Employee.objects.filter(id=id)
    emp.delete()
    context={'emp': emp} 

    return redirect("index")

    # return render(request,"Index.html",context)
