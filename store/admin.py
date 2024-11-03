from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from store.models import Category, Product
from store.models import ProductReviews, ShopReviews, ProductTags


class PriceRangeFilter(admin.SimpleListFilter):
    title = "Price Range"
    parameter_name = "price_range"

    def lookups(self, request, model_admin):
        return [
            ("0-5", "range from 0 to 5"),
            ("5-10", "range from 5 to 10"),
            ("10-15", "range from 10 to 15"),
            ("15-20", "range from 15 to 20"),
            ("20+", "range from 20"),
        ]

    def queryset(self, request, queryset):
        if self.value() == "0-5":
            return queryset.filter(
                product_price__gte=0,
                product_price__lte=5,
            )
        if self.value() == "5-10":
            return queryset.filter(
                product_price__gte=5,
                product_price__lte=10,
            )
        if self.value() == "10-15":
            return queryset.filter(
                product_price__gte=10,
                product_price__lte=15,
            )
        if self.value() == "15-20":
            return queryset.filter(
                product_price__gte=15,
                product_price__lte=20,
            )
        if self.value() == "20+":
            return queryset.filter(
                product_price__gte=20,
            )


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin, admin.ModelAdmin):
    list_display = (
        'tree_actions',
        'indented_title',
    )
    list_display_links = (
        'indented_title',
    )
    list_filter = ('parent',)
    list_select_related = ('parent',)
    prepopulated_fields = {"slug": ("category_name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'product_name',
        'product_price',
        'product_quantity',
        'get_total_price'
    )
    list_filter = [PriceRangeFilter]
    search_fields = ('product_name', 'product_category__category_name')
    list_per_page = 10
    prepopulated_fields = {"slug": ("product_name",)}

    @admin.display(description="ჯამური ფასი")
    def get_total_price(self, obj):
        return obj.product_price*obj.product_quantity


@admin.register(ProductReviews)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'date')
    search_fields = ('review',)
    list_per_page = 10


admin.site.register(ShopReviews)
admin.site.register(ProductTags)
