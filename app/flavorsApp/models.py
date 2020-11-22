from django.db import models

class Flavor(models.Model):
    name = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name