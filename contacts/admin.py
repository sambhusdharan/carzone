from django.contrib import admin
from . models import *
# Register your models here.

class Contactadmin(admin.ModelAdmin):
    list_display = ('id','first_name','car_id','customer_need','car_title','city','email','phone','user_id')
    list_display_links = ('id','first_name','car_id','car_title')
    search_fields = ('id','first_name','car_id','customer_need','car_title','city','email','phone','user_id')
    list_per_page = 20
admin.site.register(Contact,Contactadmin)

