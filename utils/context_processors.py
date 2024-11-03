from django.db.models import Count, F, Sum
from django.db.models.functions import Round
from order.models import Cart, CartItem
from store.models import Category


def custom_context(request):
    if 'admin' in request.META['PATH_INFO']:
        return {}
    else:
        cart = (
            Cart.objects.filter(
                user__id=request.user.id
            ).select_related("user")
        )
        categories = Category.objects.annotate(
            count=(Count('product') + Count('children__product'))
        ).filter(parent__isnull=True)
        cart_count = cart.aggregate(count=Count("cartitem")).get("count")

        context = {
            "cart_count": cart_count,
            "categories_root": categories,
            "param": request.GET,
        }

        if 'product' in request.META['PATH_INFO']:
            context.update({
                "categories": categories
            })

        if 'order' in request.META['PATH_INFO']:
            try:
                queryset = (
                    CartItem.objects.annotate(
                        total_price=Round(
                            F("product_quantity") * F("product__product_price")
                        )
                    ).filter(
                        cart__user_id=request.user.id
                    ).select_related("product"))

                subtotal = queryset.aggregate(
                    total=Sum("total_price")
                ).get("total")

                total = subtotal + cart.first().flat_rate
            except TypeError:
                subtotal = 0
                total = 0
            context.update(
                {
                    "total": total,
                    "subtotal": subtotal,
                    "flat_rate": cart.first().flat_rate
                }
            )
        return context
