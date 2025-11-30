from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    pass 


class ProductsCategory(models.Model):
    name = models.CharField(_("Category Name"), max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name =_("Product Category")
        verbose_name_plural = _("Product Categories")
   
    def __str__(self):
        return self.name
    

class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.ForeignKey(ProductsCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/', blank=True)
    desc = models.TextField(_("Description"))    

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name
    
    
    


class Order(models.Model):
    PENDING = "P"
    COMPLETED = "C"

    STATUS_CHOICES = (
        (PENDING, _("pending")), 
        (COMPLETED, _("completed"))
        )
    
    user = models.ForeignKey(User, related_name="orders", on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=PENDING)

    def __str__(self):
        return f"Ordered by {self.user.username}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, related_name="order_items", on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Products, related_name="product_orders", on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    @property
    def item_subtotal(self):
        return self.product.price * self.quantity