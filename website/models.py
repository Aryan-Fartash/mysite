from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=225)
    subject=models.CharField(max_length=225)
    email=models.EmailField()
    message=models.TextField()
    created_date=models.DateField(auto_now_add=True)
    updated_date=models.DateField(auto_now=True)
