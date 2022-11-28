from django.db import models

# Create your models here.

class StudentContact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=30)
    message = models.TextField(max_length=200)
    def __str__(self):
        return self.name