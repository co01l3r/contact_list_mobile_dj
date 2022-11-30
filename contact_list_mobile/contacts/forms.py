from django import forms
from .models import Contact
from django.forms.widgets import NumberInput
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from datetime import datetime


class ContactForm(forms.ModelForm):

    name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder': 'John Doe',
    }))
    phone = PhoneNumberField(required=False, widget=PhoneNumberPrefixWidget(initial='CZ', attrs={
        'type': 'tel',
        'placeholder': '123456789',
        'class': 'phone_number',
    }))
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={
        'placeholder': 'john.doe@email.com',
    }))
    web = forms.URLField(required=False, widget=forms.URLInput(attrs={
        'placeholder': 'www.johndoe.com',
    }))
    note = forms.CharField(required=False, widget=forms.Textarea(attrs={
        'placeholder': 'personal note',
        'rows': 3,
        'cols': 28,
    }))
    birthday = forms.DateField(required=False, widget=NumberInput(attrs={
        'type': 'date',
        'max': datetime.now().date(),
    }))

    class Meta:
        model = Contact
        fields = '__all__'
