from django.db import models
from pizzasApp.models import Pizza
from clientsApp.models import Client 

from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

# Create your models here.
class Order(models.Model):

    STATUS_CHOICES = (
        ('in_queue', 'In Queue'),
        ('in_production', 'In Production'),
        ('on_delivery', 'On Delivery'),
        ('delivered', 'Delivered'),
    )

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    pizzas = models.ManyToManyField(Pizza, related_name="order_pizzas")
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='in_queue')
    value = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True, default=0)

    #For track action
    created_at = models.DateTimeField(auto_now_add=True)
    in_production_at = models.DateTimeField(null=True, blank=True)
    on_delivery_at = models.DateTimeField(null=True, blank=True)
    delivered_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.client.name + ' - ' + self.status

@receiver(pre_save, sender=Order)
def update_order_value(sender, instance, *args, **kwargs):
    if instance._state.adding is False:
        order = Order.objects.get(id=instance.id)
        pizzas = order.pizzas.all()
        total_value = 0
        for pizza in pizzas:
            total_value += pizza.value
        instance.value = total_value