from django.db import models
from django.utils.translation import gettext_lazy as _ 
from products.models import Order


class Payment(models.Model):

    PENDING = "P"
    COMPLETED = "C"
    FAILED = "F"

    STATUS_CHOICES = (
    (PENDING, _("pending")),
    (COMPLETED, _("completed")),
    (FAILED, _("failed")),

    )

    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=PENDING)
    payment_intent_id = models.CharField(max_length=255)
    amount = models.IntegerField()
    currency = models.CharField(max_length=10, default="usd")
    order = models.ForeignKey(
        Order, related_name="payment", on_delete=models.CASCADE,null=True, blank=True
    )


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = _("Payment")
        verbose_name_plural = _("Payments")

    def __str__(self):
        return self.payment_intent_id
