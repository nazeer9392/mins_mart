from django.contrib import admin
from . models import Product,Cart

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    model=Product
    list_display=['id','name','price','image','created_at']
    
admin.site.register(Product,ProductAdmin)
    
class Cartadmin(admin.ModelAdmin):
    model=Cart
    list_display=['id','name','price','image','quantity','totalprice']
    
    
admin.site.register(Cart,Cartadmin)