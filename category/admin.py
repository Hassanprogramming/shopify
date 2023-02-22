from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(CustomerUser)
admin.site.register(CategoryProduct)
admin.site.register(CategoryOrder)
admin.site.register(CategoryOrderItem)
admin.site.register(CategoryShippingAddress)