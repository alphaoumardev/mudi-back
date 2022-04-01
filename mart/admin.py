from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .entity.orders_entity import *
from .entity.products_entity import *
from .entity.customers_entity import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', "brand", "category", "stock", "price", "image_preview")


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("user_name", "phone_number", "country", "city", "address", "avatar_preview")


# Register your models here.
class Variants(admin.TabularInline):
    model = Variant


class FuturedImg(admin.TabularInline):
    model = FuturedImages


class ProductAdmins(admin.ModelAdmin):
    inlines = [Variants, FuturedImg]
    # list_display = ['color_name']


admin.site.register(CustomerProfile, CustomerAdmin)

admin.site.register(Genre)
admin.site.register(Types)
admin.site.register(Category)

admin.site.register(Product,   ProductAdmins) #ProductAdims

admin.site.register(Variant)
admin.site.register(FuturedImages)
admin.site.register(SizesOption)
admin.site.register(ColorsOption)
admin.site.register(Wishlist)
admin.site.register(Sliders)
admin.site.register(Comments)

# admin.site.register(OrderItems)
# admin.site.register(CartItem)
# admin.site.register(OrderDetails)
# admin.site.register(PaymentDetails)
# admin.site.register(UserPay)
