from django import forms
from django.core.exceptions import ValidationError
from order.models import CartItem
from store.models import Product


class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['product', 'product_quantity']

    def clean(self):
        cleaned_data = super().clean()
        product: Product = cleaned_data.get("product")
        quant = product.product_quantity

        if quant < cleaned_data.get("product_quantity"):
            raise ValidationError(
                f"Product of {quant} cannot be added"
            )

        return cleaned_data
