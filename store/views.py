from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.db.models import Count
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.cache import cache_page
from django.views.generic import DetailView, ListView, TemplateView, FormView
from mixins.search_mixin import SearchMixin
from store.forms import ContactForm
from store.models import Product, ProductReviews
from store.models import Category, ShopReviews, ProductTags


class IndexView(SearchMixin, ListView):
    model = ShopReviews
    template_name = "homepage/index.html"
    queryset = ShopReviews.objects.select_related("user")
    context_object_name = "reviews"


@method_decorator(cache_page(60 * 1), name="dispatch")
class CategoryListingsView(ListView):
    """
    filters:
    'q' -> search
    't' -> tags
    'p' -> price
    'fruitlist' -> sorting
    """
    model = Product
    template_name = "shop/shop.html"
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.request.GET.get('q'):
            queryset = queryset.filter(
                product_name__icontains=self.request.GET.get('q')
            ).prefetch_related("tags")

        if self.request.GET.get('t') or self.request.GET.get('p'):
            tags = None
            if self.request.GET.get('t'):
                tags = str(self.request.GET.get('t'))

            queryset = queryset.filter(
                product_price__lte=float(self.request.GET.get('p'))
            ).prefetch_related("tags")

            if tags:
                queryset = queryset.filter(tags=tags).prefetch_related("tags")

        if self.request.GET.get("fruitlist"):
            if self.request.GET.get("fruitlist") == "2":
                queryset = queryset.order_by("product_price")

        category_slug = self.kwargs.get("slug")
        if category_slug:
            category = Category.objects.filter(slug=category_slug)
            categories = category.get_descendants(include_self=True)
            queryset = (
                queryset
                .filter(product_category__in=categories)
                .prefetch_related("tags")
            )
        return queryset.prefetch_related("product_category", "tags")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.filter(parent__isnull=True)
        product_tags = ProductTags.objects.all()

        category_slug = self.kwargs.get("slug")
        if category_slug:
            category = Category.objects.filter(slug=category_slug)
            categories = (
                category
                .get_descendants(include_self=False)
                .annotate(count=Count("product") + Count('children__product'))
            )
        else:
            categories = (
                categories
                .get_descendants(include_self=True)
                .annotate(count=Count('product') + Count('children__product'))
                .filter(parent__isnull=True)
            )
        context["categories"] = categories
        context["product_tags"] = product_tags
        return context


class ContactView(SearchMixin, FormView):
    template_name = "contact/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("store:contact")

    def form_valid(self, form):
        sender_name = form.cleaned_data["sender_name"]
        sender_email = form.cleaned_data["sender_email"]
        message = form.cleaned_data["message"]
        send_mail(
            f"New Message from {sender_name} {sender_email}",
            message,
            settings.EMAIL_HOST_USER,
            ["kristigaphrindashvili@gmail.com"],
            # Enter your Email for testing. Gmail won't create
            # another one for me without a phone number
            fail_silently=False,
        )
        messages.success(self.request, 'Message sent successfully!')
        return super().form_valid(form)


class ProductView(SearchMixin, DetailView):
    model = Product
    template_name = "product_detail/shop-detail.html"
    pk_url_kwarg = "id"
    queryset = Product.objects.prefetch_related("product_category", "tags")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_reviews = ProductReviews.objects.filter(
            product=self.object
        ).select_related("user")
        quantity = 1

        context["reviews"] = product_reviews
        context["quantity"] = quantity
        return context


class PageNotFound(TemplateView):
    template_name = '404.html'


# For testing set DEBUG to False and visit "test500/"
class InternalServerError(View):
    def get(self, request, *args, **kwargs):
        raise Exception
