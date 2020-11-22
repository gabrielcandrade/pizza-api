from django.db import models
from flavorsApp.models import Flavor
from sizesApp.models import Size

# Create your models here.
class Pizza(models.Model):
    flavor = models.ForeignKey(Flavor, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    value = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.flavor.name + ' - ' + self.size.name + ' - ' + str(self.quantity)

    def save(self, *args, **kwargs):
        self.value = (self.flavor.value + self.size.value) * self.quantity
        return super(Pizza, self).save(*args, **kwargs)