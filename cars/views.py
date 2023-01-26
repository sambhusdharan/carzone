from django.shortcuts import render,redirect,get_object_or_404
from .models import car,carlatest
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.
def cars(request):
    cars_featur=car.objects.order_by('-created_date').filter(is_featured=True)
    cars_lates = carlatest.objects.order_by('-created_date').filter(sale=True)
    model_feature = car.objects.values_list('model',flat=True).distinct()#(flat=True)When grabbing a single values from the db, you can pass`flat=true` which will just give you back single values, instead of tuples
    model_latest = carlatest.objects.values_list('model', flat=True).distinct()
    city_feature = car.objects.values_list('city', flat=True).distinct()
    city_latest = carlatest.objects.values_list('city',flat=True).distinct()
    year_feature = car.objects.values_list('year', flat=True).distinct()
    year_latest = carlatest.objects.values_list('year', flat=True).distinct()
    body_feature = car.objects.values_list('body_style', flat=True).distinct()
    body_latest = carlatest.objects.values_list('body_style', flat=True).distinct()
    transmission_feature = car.objects.values_list('transmission', flat=True).distinct()
    transmission_latest = carlatest.objects.values_list('transmission',flat=True).distinct()
    return render(request,'car/cars.html',{'carf':cars_featur,'carlat':cars_lates,'model_feature':model_feature,'model_latest':model_latest,'city_feature':city_feature,'city_latest':city_latest,'year_feature':year_feature,'year_latest':year_latest,'body_feature':body_feature,'body_latest':body_latest,'transmission_feature':transmission_feature,'transmission_latest':transmission_latest})

@login_required(login_url = 'login')
def car_detail(request,id):
  car_detail=get_object_or_404(car,id=id)
  return render(request,'car/car_detail.html',{'cardetail':car_detail})
@login_required(login_url = 'login')
def latest_car(request,id):
    latest = get_object_or_404(carlatest, id=id)
    return render(request, 'car/latest_detail.html', {'latest': latest})

def search(request):
    featu_search = car.objects.order_by('-created_date').filter(is_featured=True)
    lates_search = carlatest.objects.order_by('-created_date').filter(sale=True)

    model_feature = car.objects.values_list('model',flat=True).distinct()#(flat=True)When grabbing a single values from the db, you can pass`flat=true` which will just give you back single values, instead of tuples
    model_latest = carlatest.objects.values_list('model', flat=True).distinct()
    city_feature = car.objects.values_list('city', flat=True).distinct()
    city_latest = carlatest.objects.values_list('city',flat=True).distinct()
    year_feature = car.objects.values_list('year', flat=True).distinct()
    year_latest = carlatest.objects.values_list('year', flat=True).distinct()
    body_feature = car.objects.values_list('body_style', flat=True).distinct()
    body_latest = carlatest.objects.values_list('body_style', flat=True).distinct()
    transmission_feature = car.objects.values_list('transmission', flat=True).distinct()
    transmission_latest = carlatest.objects.values_list('transmission',flat=True).distinct()


    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            featu_search = car.objects.all().filter(Q(description__icontains=keyword)|Q(cartitle__icontains=keyword)|Q(body_style__icontains=keyword)|Q(city__icontains=keyword)|Q(state__icontains=keyword)|Q(engine__icontains=keyword)|Q(year__icontains=keyword)|Q(model__icontains=keyword))
            print("feature",featu_search)
            lates_search = carlatest.objects.all().filter(Q(description__icontains=keyword)|Q(cartitle__icontains=keyword)|Q(body_style__icontains=keyword)|Q(city__icontains=keyword)|Q(state__icontains=keyword)|Q(engine__icontains=keyword)|Q(year__icontains=keyword)|Q(model__icontains=keyword))
            print("latest",lates_search)
    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            featu_search = car.objects.all().filter(model__iexact=model)
            lates_search = carlatest.objects.all().filter(model__iexact=model)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            featu_search = car.objects.all().filter(city__iexact=city)
            lates_search = carlatest.objects.all().filter(city__iexact=city)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            featu_search = car.objects.all().filter(year__iexact=year)
            lates_search = carlatest.objects.all().filter(year__iexact=year)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            featu_search = car.objects.all().filter(body_style__iexact=body_style)
            lates_search = carlatest.objects.all().filter(body_style__iexact=body_style)

    if 'transmission' in request.GET:
        transmission = request.GET['transmission']
        if transmission:
            featu_search = car.objects.all().filter(transmission__iexact=transmission)
            lates_search = carlatest.objects.all().filter(transmission__iexact=transmission)

    # if 'min_price' in request.GET:
    #     min_price = request.GET['min_price']
    #     max_price = request.GET['max_price']
    #     if max_price:
    #         featu_search = car.objects.all().filter(price__gte = min_price, price__lte = max_price)
    #         print('feature price',featu_search)
    #         lates_search = carlatest.objects.all().filter(price__gte = min_price, price__lte = max_price)
    #         print('latest price', lates_search)

    return render(request,'pages/search.html',{'feature_search':featu_search,'latest_search':lates_search,'model_feature':model_feature,'model_latest':model_latest,'city_feature':city_feature,'city_latest':city_latest,'year_feature':year_feature,'year_latest':year_latest,'body_feature':body_feature,'body_latest':body_latest,'transmission_feature':transmission_feature,'transmission_latest ':transmission_latest })