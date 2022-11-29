from django import forms
from .models import Contact
from django.forms.widgets import NumberInput
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class ContactForm(forms.ModelForm):

    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'John Doe',}))
    phone = PhoneNumberField(required=False, widget=PhoneNumberPrefixWidget(initial='CZ', attrs={'type': 'tel', 'placeholder': '123456789', 'class': 'phone_number'}))
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'placeholder': 'johndoe@email.com'}))
    web = forms.URLField(required=False, widget=forms.TextInput(attrs={'placeholder': 'www.johndoe.com'}))
    note = forms.CharField(required=False, widget=forms.Textarea(attrs={'placeholder': 'personal note', 'rows': 3, 'cols': 30}))
    # birthday = forms.DateField(widget=forms.SelectDateWidget(years=range(1940, 2022)))
    birthday = forms.DateField(required=False, widget=NumberInput(attrs={'type': 'date'}))

    class Meta:
        model = Contact
        fields = '__all__'
