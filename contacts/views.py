from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
# Create your views here.
def inquiry(request):
    if request.method == 'POST':
        car_id=request.POST['car_id']
        car_title = request.POST['car_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name=request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message=request.POST['message']

        if request.user.is_authenticated:
            userid=request.user.id
            has_contacted=Contact.objects.all().filter(car_id=car_id,user_id=userid)
            if has_contacted:
                messages.error(request,"You had already registered. We will contact you soon")
                return redirect('car')

        customer=Contact(car_id=car_id,car_title=car_title,user_id=user_id,first_name=first_name,last_name=last_name,customer_need=customer_need,city=city,state=state,email=email,phone=phone,message=message)
        admin_detail=User.objects.get(is_superuser=True)
        admin_email=admin_detail.email
        send_mail(
            'New Car inquiry',
            'You have a new inquiry for the car with ID: ' + car_id+ ' and car Name: '+ car_title+ ' Please login to admin pannel for more detail' ,
            'sambhusdharan@gmail.com', #from email address
            [admin_email], #To email address
            fail_silently=False,
                 )

        customer.save()
        messages.success(request,"YOU HAVE SUBMITTED THE FORM AND WE WILL CONTACT YOU SOON")
        return redirect('car')
        # return redirect('/car/',+ car_id)