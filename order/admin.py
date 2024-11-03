from django.contrib import admin
from order.models import Checkout, Cart, CartItem


@admin.register(CartItem)
class CartItemsAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'product_quantity', 'cart')
    list_prefetch_related = ('product', 'cart')
    search_fields = ('id', 'product__product_name')
    list_per_page = 10


@admin.register(Checkout)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_date', 'product_cart')
    list_filter = ('order_date',)
    list_prefetch_related = ('product_cart',)
    search_fields = ('id',)
    list_per_page = 10


@admin.register(Cart)
class UserCartAdmin(admin.ModelAdmin):
    list_display = ('user', 'flat_rate')
    list_select_related = ('user',)
    list_per_page = 10
