from django.contrib import admin
from .models import VehicleModel,BookingModel
# Register your models here.


@admin.register(VehicleModel)
class VehicleModelAdmin(admin.ModelAdmin):
    list_display = ["v_type","v_class","duration", "price", "to_location", "from_location", "provider"]
    list_display.reverse()

@admin.register(BookingModel)
class BookingModelAdmin(admin.ModelAdmin):
    list_display = ["v_type","total","to_location", "from_location", "provider", "gender", "email", "mobile", "lname", "fname", "user","id"]
    list_display.reverse()