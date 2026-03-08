from django.contrib import admin

# Register your models here.

from .models import Category,Product,Cart,Orders,User_Detail

admin.site.register(Category)
admin.site.register(Product)

admin.site.register(Cart)
admin.site.register(Orders)


admin.site.register(User_Detail)


