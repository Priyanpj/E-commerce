from django.contrib import admin
from. models import feature_products
from. models import *
# Register your models here.
class catadmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
class proAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(feature_products,proAdmin)
admin.site.register(category,catadmin)
# admin.site.register(products)