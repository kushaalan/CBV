from django.db import models
from django.urls import reverse

# Create your models here.
class company(models.Model):
    name = models.CharField(max_length=100)
    ceo = models.CharField(max_length=100)
    est_year = models.IntegerField()
    origin = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="logos/",blank=True,null=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("details", kwargs={"pk": self.pk})

class product(models.Model):
    prod_name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    price = models.IntegerField()
    fuel_type = models.CharField(max_length=50)
    cc = models.IntegerField()
    mileage = models.IntegerField()
    prod_img = models.ImageField(upload_to="prodimg/",blank=True,null=True)
    company = models.ForeignKey(company, related_name="companies",on_delete=models.CASCADE)
