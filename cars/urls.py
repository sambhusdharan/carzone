"""carzone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path,include
from . import views
urlpatterns = [
    path('cars',views.cars,name='car'),
    path('<int:id>',views.car_detail,name='car_detail'),
    path('car/<int:id>',views.latest_car,name='latest_car'),
    path('search',views.search,name='search')
]









# video  26. Make Cars Navlink & Correct Logo
