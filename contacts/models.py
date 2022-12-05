from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50, blank=False)
    phone = PhoneNumberField(null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    web = models.URLField(max_length=300, null=True, blank=True)
    note = models.CharField(max_length=400, null=True, blank=True)
    birthday = models.DateField(auto_now_add=False, auto_now=False, null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

