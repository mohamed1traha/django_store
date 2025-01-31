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
    list_per_page = 20
    
    def has_change_permission(self, request, obj = None):
        return False

    def has_add_permission(self, request):
        return False




