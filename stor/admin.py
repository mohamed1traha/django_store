from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Category)
class CategoryAAdmin(admin.ModelAdmin):
    list_per_page = 20



@admin.register(models.Author)
class AutherAdmin(admin.ModelAdmin):
    list_per_page = 20



@admin.register(models.Product)
class ProductAAdmin(admin.ModelAdmin):
    list_per_page = 20



@admin.register(models.Slider)
class SliderAdmin(admin.ModelAdmin):
    list_per_page = 20



@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','amount','items','email','payment_method','created_at',]
    list_per_page = 20
    list_select_related = ['transaction']

    
    def has_change_permission(self, request, obj = None):
        return False

    def has_add_permission(self, request):
        return False

    def amount(self, obj):
        if obj.transaction:
            return obj.transaction.amount
        return 'لا توجد معاملة'

    
    def items(self,obj):
        if obj.transaction:
            return len(obj.transaction.items)
        return 'لا توجد معاملة'
    
    def email(self,obj):
        if obj.transaction:
            return obj.transaction.customer_email
        return 'لا توجد معاملة'
    
    def payment_method(self,obj):
        if obj.transaction:
            return obj.transaction.get_payment_method_display()
        return 'لا توجد معاملة'





