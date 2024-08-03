from django.contrib import admin

from .models import *

class CatogoryAdmin(admin.ModelAdmin):
    list_display = ('name','image','description')

admin.site.register(Catogory,CatogoryAdmin)
admin.site.register(Products)
admin.site.register(ShippingAddress)
admin.site.register(Orders)
