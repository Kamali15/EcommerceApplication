from django.contrib import admin
from .models import Product,Category,Customer,Order
# Register your models here.
admin.site.register([Product,Category,Customer,Order])