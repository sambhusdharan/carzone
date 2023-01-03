from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages,auth
from django.contrib.auth.models import User
from contacts.models import Contact
from django.contrib.auth.decorators import login_required
from cars.models import *
# Create your views here.
def login(request):
    if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']
       user = auth.authenticate(username=username, password=password)
       if user is not None:
            auth.login(request,user)
            messages.success(request,"successfully logedin")
            return render(request,'accounts/dashboard.html',{'user':user})
       else:
           messages.error(request,"invalid username and password")
           return redirect("login")
    else:
       return render(request,'accounts/login.html')

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password :
            if User.objects.filter(username=username).exists():
                messages.error(request,"username already exists")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,"email already exists")
                    return redirect("register")
                else:
                    user=User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password)
                    auth.login(request,user)
                    messages.success(request,"you are now logged in")
                    return render(request,"accounts/dashboard.html",{'user':user})
                    user.save()
                    messages.success(request,"you registered successfully")
                    return redirect("login")
        else:
            messages.error(request,"password doesn't match")
            return redirect('register')
    else:
        return render(request,'accounts/register.html')
@login_required(login_url = 'login')
def dashboard(request):

    needed_value=Contact.objects.values('car_title').filter(user_id=request.user.id)
    print(needed_value)
    carval=carlatest.objects.values('cartitle')
    print(carval)
    if carval:
        if needed_value:
            data = Contact.objects.order_by('-created_date').filter(user_id=request.user.id)
            return render(request, 'accounts/dashboard.html', {'data': data})
            print("found")
    else:
        car = Contact.objects.order_by('-created_date').filter(user_id=request.user.id)
        return render(request, 'accounts/dashboard.html', {'cardata': car})
        print("not")
    # else:
    #     data = Contact.objects.order_by('-created_date').filter(user_id=request.user.id)
    #     return render(request, 'accounts/dashboard.html', {'val': data})

    # data = Contact.objects.order_by('-created_date').filter(user_id=request.user.id)
    # return render(request, 'accounts/dashboard.html', {'data': data})






def logout(request):
    if request.method == 'POST':
     auth.logout(request)
    return redirect('login')

def delete(request,id):
    car_del = Contact.objects.get(car_id=id)
    car_del.delete()
    return redirect('dashboard')
