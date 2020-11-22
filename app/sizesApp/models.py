from django.db import models

# Create your models here.
class Size(models.Model):
    name = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=5, decimal_places=2)
    slices = models.IntegerField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name