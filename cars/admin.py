from django.contrib import admin
from .models import car,carlatest
from django.utils .html import format_html
# Register your models here.
class car_admin(admin.ModelAdmin):
    def image(self,object):
        return format_html('<img src="{}" width=40px style="border-radius:50px" />'.format(object.car_photo_1.url))
    list_display =('id','cartitle','image','state','city','color','model','year','condition','price','engine','milage','is_featured')
    list_display_links =('cartitle','image')
    search_fields = ('cartitle','city','model','year','price','body_style','milage','fuel_type')
    list_editable = ('is_featured',)
    list_filter = ('city','model','fuel_type','body_style')
admin.site.register(car,car_admin)

class latest(admin.ModelAdmin):
    def photo(self,object):
        return format_html('<img src="{}" width=45px style="border-radius:50px" />'.format(object.car_photo_1.url))
    list_display =('id','cartitle', 'photo','state','city','color','model','year','condition','price','engine','milage','sale')
    list_display_links = ('cartitle','photo')
    search_fields = ('cartitle', 'city', 'model', 'year', 'price', 'body_style', 'milage', 'fuel_type')
    list_editable = ('sale',)
admin.site.register(carlatest,latest)