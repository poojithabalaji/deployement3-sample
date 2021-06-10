from django.db import models
from django.urls import reverse

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=120)
    age =models.PositiveIntegerField()
    school =models.CharField(max_length=120)

    def get_absolute_url(self):
        return reverse('mycbvapp:details', kwargs={'pk':self.pk})
