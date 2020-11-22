from django.db import models
from addressApp.models import Address

# Create your models here.
class Client(models.Model):
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    birth_date = models.DateField(blank=True, null=True) # For promotions
    client_since = models.DateTimeField(auto_now_add=True)
    is_vip = models.BooleanField(default=False)

    def __str__(self):
        return self.name