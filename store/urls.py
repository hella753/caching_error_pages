from django.urls import path
from . import views


app_name="store"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("category/", views.CategoryListingsView.as_view(), name="category_listings"),
    path("category/<slug:slug>/", views.CategoryListingsView.as_view(), name="category_listings"),
    path("product/<slug:slug>/", views.ProductView.as_view(), name="product"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("test500/", views.InternalServerError.as_view(), name="internal_server_error")
]
