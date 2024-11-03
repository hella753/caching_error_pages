from django.db.models.signals import post_save
from django.dispatch import receiver
from user.models import User
from order.models import Cart


@receiver(post_save, sender=User)
def create_cart_for_user(sender, **kwargs):
    """
    This signal checks if the user is already registered
    on the website and if not creates a cart for the user.
    """
    user_obj = kwargs.get("instance")

    try:
        has_cart = user_obj.cart
    except:
        has_cart = False

    if not user_obj.is_superuser and not has_cart:
        cart = Cart(user=user_obj, flat_rate=5)
        cart.save()
        print(f"cart has been created {user_obj}")
