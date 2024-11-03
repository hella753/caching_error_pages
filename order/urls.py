from django.urls import path
from . import views

app_name = "order"
urlpatterns = [
    path("cart/", views.CartView.as_view(), name="cart"),
    path("checkout/", views.CheckoutView.as_view(), name="checkout"),
    path("add_to_cart/", views.AddToCartView.as_view(), name="add_to_cart"),
    path("delete/<int:pk>/", views.AddToCartDeleteView.as_view(), name="delete_from_cart")
]
