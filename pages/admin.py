from django.contrib import admin
from .models import Team
from django.utils.html import format_html #to use html basrd tag in our django
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def photo(self,object): #inorder to add photo to our admin pannel
        return  format_html('<img src="{}" width=40px  style="border-radius:50px" />'.format(object.img.url))
    # photo.short_description='image' #with this we can change the title photo to image
    list_display = ('id','first_name','last_name','photo','designation','created_date')
    # list_editable = ('first_name','img','last_name')
    list_display_links = ('first_name','photo','designation')
    search_fields = ('id','first_name','last_name','designation')
    list_filter = ('designation',)# comma after designation is very important because its a tuple
admin.site.register(Team,TeamAdmin)