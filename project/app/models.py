from django.db import models

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    description = models.TextField()

    def __str__(self):
        return self.name