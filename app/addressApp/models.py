from django.db import models

# Create your models here.
class Address(models.Model):
    line1 = models.CharField(max_length=150)
    line2 = models.CharField(max_length=150, blank=True, null=True)
    city = models.CharField(max_length=50)
    state_province = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=50)
    country = models.CharField(max_length=25)

    def __str__(self):
        return self.line1