from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255, default='Default subject')
    message = models.TextField(default='default message')
    email = models.EmailField(default='Default email')
    created_date = models.DateTimeField(auto_now= True)
    updated_date = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.name

