# from django.contrib import admin
# from .models import related models
from django.contrib import admin
from .models import CarMake, CarModel

class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'type', 'year')

class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)

# Register your models here.

# CarModelInline class

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here
