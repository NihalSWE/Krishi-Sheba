from django.contrib import admin
from .models import (Customer,Product,AddCart,Order,Machinery,Rent_Request)
from django.utils.html import format_html
from django.urls import reverse
# Register your models here.
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['id','user','name','phone','locality','city','district','gender']
    search_fields=('name','gender','district')

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id','title','selling_price','description','brand','category','product_image']
    search_fields=('title','selling_price','brand','category')

@admin.register(AddCart)
class AddCartModelAdmin(admin.ModelAdmin):
    list_display=['id','user','product','quantity']


@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    list_display=['id','user','customer','customer_info','product','product_info','quantity','ordered_date','status']

    

    def customer_info(self,obj):
        link = reverse("admin:ProductItem_customer_change",args=[obj.customer.pk])
        return format_html('<a href="{}">{}</a>',link,obj.customer.name)

    def product_info(self,obj):
        link = reverse("admin:ProductItem_product_change",args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>',link,obj.product.title)



@admin.register(Machinery)
class MachineryModelAdmin(admin.ModelAdmin):
    list_display=['id','title','rent_perday','description','brand','product_image','is_Available']

    list_display_links = ('title','rent_perday')
    search_fields=('title','rent_perday')
    list_editable = ('is_Available',)
    
    list_per_page=25


@admin.register(Rent_Request)
class Rent_RequestModelAdmin(admin.ModelAdmin):
    list_display=['id','user_id','product_id','product_name','name','message','confirm']
   
    list_display_links=('id','name','product_name')
    search_fields=('product_name','name')
    list_editable=('confirm',)
    list_per_page=25