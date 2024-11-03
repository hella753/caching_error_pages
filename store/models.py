from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.conf import settings
from versatileimagefield.fields import VersatileImageField


class Category(MPTTModel):
    category_name = models.CharField("სახელი", max_length=100, null=True)
    parent = TreeForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="ზეკატეგორია",
        related_name="children"
    )
    slug = models.SlugField(default="", blank=True)

    class MPTTMeta:
        order_insertion_by = ['category_name']

    def __str__(self):
        return f"{self.category_name}"


class Product(models.Model):
    product_name = models.CharField("სახელი", max_length=100)
    product_price = models.DecimalField(
        "ფასი",
        max_digits=10,
        decimal_places=2
    )
    product_description = models.TextField("აღწერა", null=True, blank=True)
    product_rating = models.IntegerField("შეფასება", null=True, blank=True)
    product_image = VersatileImageField(
        "სურათი",
        help_text="ატვირთეთ ფოტოსურათი",
        blank=True,
        null=True
    )
    product_category = models.ManyToManyField(
        "Category",
        verbose_name="კატეგორია"
    )
    product_quantity = models.IntegerField("მარაგშია:", null=True, blank=True)
    country = models.CharField("country", default="Agro Farm", max_length=150)
    weight = models.PositiveIntegerField("წონა", default=1)
    slug = models.SlugField(default="", unique=True, blank=True)
    tags = models.ManyToManyField("ProductTags", blank=True)

    def __str__(self):
        return f"{self.product_name}"


class ProductReviews(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="ავტორი"
    )
    product = models.ForeignKey(
        "Product",
        on_delete=models.CASCADE,
        verbose_name="პროდუქტი"
    )
    date = models.DateField(auto_now_add=True)
    review = models.TextField("რევიუ")


class ShopReviews(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="ავტორი"
    )
    review = models.TextField("რევიუ")
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}"


class ProductTags(models.Model):
    tag_name = models.CharField(max_length=150)

    def __str__(self):
        return self.tag_name
