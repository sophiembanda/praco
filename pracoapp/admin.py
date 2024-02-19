from django.contrib import admin
from .models import User,Booking,Cancellation,HairdresserProfile,UserProfile,Service

# Register your models here.
admin.site.register(User)
admin.site.register(Booking)
admin.site.register(Cancellation)
admin.site.register(HairdresserProfile)
admin.site.register(UserProfile)
admin.site.register(Service)