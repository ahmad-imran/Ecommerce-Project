from django.contrib import admin
from App_Order.models import Cart, Order

# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "created")

admin.site.register(Cart)
