from django.contrib import admin
from .models import *
from .translation import CategoryTranslationOptions,ProductTranslationOptions
from modeltranslation.admin import TranslationAdmin
from import_export.admin import ImportExportModelAdmin
from .resources import *
@admin.register(BotUser)
class BotUserAdmin(admin.ModelAdmin):
    list_display = ['name','telegram_id','language']
    list_filter = ['language','added']
    list_per_page = 10
    search_fields = ['name','language','telegram_id']
@admin.register(Location)
class LocationsAdmin(admin.ModelAdmin):
    list_display = ['user','latitude','longitude']
    list_per_page = 10
@admin.register(Category)
class CategoryAdmin(TranslationAdmin,ImportExportModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_per_page = 10
    resource_classes = [CategoryResource]
@admin.register(SubCategory)
class SubCategoryAdmin(TranslationAdmin,ImportExportModelAdmin):
    list_display = ['name','category']
    search_fields = ['name','category__name']
    list_per_page = 10
@admin.register(Product)
class ProductAdmin(TranslationAdmin,ImportExportModelAdmin):
    list_display = ['picture','name','category','price','discount']
    search_fields  = ['name','about','category__name']
    list_per_page = 10
    list_filter = ['discount','category']
    resource_classes = [ProductResource]
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user','all_shop','all_products']
    list_per_page = 10
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order','product','quantity','shop']
    list_per_page = 10