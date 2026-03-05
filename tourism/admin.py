from django.contrib import admin
from .models import Category, Tour, Review, Booking

admin.site.register(Category)
admin.site.register(Tour)
admin.site.register(Review)
admin.site.register(Booking)
