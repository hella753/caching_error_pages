from django.conf import settings
from django.db import models
from user.models import User


class Checkout(models.Model):
    order_notes = models.TextField("შეკვეთის დეტალები", null=True, blank=True)
    order_date = models.DateField("შეკვეთის თარიღი", auto_now_add=True)
    product_cart = models.ForeignKey(
        "order.Cart",
        on_delete=models.CASCADE,
        verbose_name="მომხმარებლის კალათა",
    )

    def __str__(self):
        return f"Order {self.id}"


class Cart(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name="მომხმარებელი"
    )
    flat_rate = models.IntegerField("მიტანა", default=5)

    def __str__(self):
        return f"{self.user}"


class CartItem(models.Model):
    product = models.ForeignKey(
        "store.Product",
        on_delete=models.CASCADE,
        verbose_name="პროდუქტი"
    )
    product_quantity = models.IntegerField("რაოდენობა")
    cart = models.ForeignKey(
        "order.Cart",
        on_delete=models.CASCADE,
        verbose_name="კალათა"
    )
