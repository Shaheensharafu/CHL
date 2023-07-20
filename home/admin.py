from django.contrib import admin

# Register your models here.
from .models import staffs,Doctor,booking

admin.site.register(staffs)
admin.site.register(Doctor)

class BookingAdmin(admin.ModelAdmin):
    list_display=('id','p_name','p_phone','p_email','doc_name','booking_date','booked_on')

admin.site.register(booking,BookingAdmin)
