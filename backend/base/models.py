from django.db import models

# Create your models here.

class Stores(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    manager_email=models.EmailField()
    creation_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
        