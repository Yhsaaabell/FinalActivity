from django.db import models

# Create your models here.
class Record(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    check_in = models.CharField(max_length=50)
    check_out = models.CharField(max_length=50)
    payment_method = models.CharField(max_length=10)
    
    def __str__(self):
        return(f"{self.first_name} {self.last_name}")
