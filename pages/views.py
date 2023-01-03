from django.shortcuts import render,redirect
from .models import  Team
from cars.models import car,carlatest
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail

# Create your views here.
def home(request):
    team=Team.objects.all()
    features_cars = car.objects.order_by('-created_date').filter(is_featured=True)
    car_latest=carlatest.objects.order_by('-created_date').filter(sale=True)
    # search_featured=car.objects.values('model','city','year','body_style')
    # search_latest=carlatest.objects.values('model','city','year','body_style')
    model_feature = car.objects.values_list('model',flat=True).distinct()
    model_latest = carlatest.objects.values_list('model', flat=True).distinct()
    city_feature = car.objects.values_list('city', flat=True).distinct()
    city_latest = carlatest.objects.values_list('city',flat=True).distinct()
    year_feature = car.objects.values_list('year', flat=True).distinct()
    year_latest = carlatest.objects.values_list('year', flat=True).distinct()
    body_feature = car.objects.values_list('body_style', flat=True).distinct()
    body_latest = carlatest.objects.values_list('body_style', flat=True).distinct()

    return render(request,'pages/home.html',{'team':team,'feature':features_cars,'latest':car_latest,'model_feature':model_feature,'model_latest':model_latest,'city_feature':city_feature,'city_latest':city_latest,'year_feature':year_feature,'year_latest':year_latest,'body_feature':body_feature,'body_latest':body_latest})

def about(request):
    team=Team.objects.all()
    return render(request,'pages/about.html',{'team':team})

def services(request):
    return render(request,'pages/service.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']
        subject_info='you have a new message with subject'+subject,
        message_info = 'You have a message from \n Name :' +name+ '\n  Email :' +email+ '\n  Phone Number :' +phone+ ' \n Message: '+message
        admin_detail = User.objects.get(is_superuser=True)
        admin_email = admin_detail.email

        send_mail(
            subject_info,
            message_info,
            'sambhusdharan@gmail.com', #from email address
            [admin_email], #To email address
            fail_silently=False,
        )

        messages.success(request,"Your message is submitted ,We will contact you soon")
        return redirect('contact')
    return render(request,'pages/contact.html')