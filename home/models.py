from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.CharField(max_length=254)
    subject = models.CharField(max_length=35)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.first_name
    
