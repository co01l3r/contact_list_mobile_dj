from django.db import models
from birthday import BirthdayField, BirthdayManager
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=300, blank=False)
    phone = PhoneNumberField(null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    web = models.CharField(max_length=400, null=True, blank=True)
    note = models.CharField(max_length=500, null=True, blank=True)
    birthday = BirthdayField(auto_now_add=False, auto_now=False, null=True, blank=True)
    objects = BirthdayManager()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
