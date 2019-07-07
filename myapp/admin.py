from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product, Category, Client, Order

def add_stock(modeladmin, request, queryset):
    for product in queryset:
        product.stock = product.stock +50
        product.save()
    add_stock.short_description = 'Stock add 50'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'available')
    actions = [add_stock]

# class ClientAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name', 'city', 'interested_in')
#
#     def interested(self,obj):
#         obj_list = obj.category
#         return obj_list

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Client)
# admin.site.register(Client, ClientAdmin)
admin.site.register(Order)














# from django.contrib import admin

#
# # Register your models here.
# # Register your models here.
#
# from django.contrib import admin
# from .models import Product, Category, Client, Order
#
# # Register your models here.
# admin.site.register(Product)
# admin.site.register(Category)
# admin.site.register(Client)
# admin.site.register(Order)

