from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from django.shortcuts import redirect
from .models import Contact
import datetime


# Create your views here.
def index(request):
    contacts = Contact.objects.all()

    context = {'contacts': contacts}
    return render(request, 'index.html', context)


def add_contact(request):
    form = ContactForm()

    if request.method == 'POST':

        print(request.POST)

        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact added')
            # return redirect(request, 'index')

    context = {'form': form}
    return render(request, 'contacts/contact_form.html', context)


# def show_contact(request):
#     birthdays_upcoming = Contact.objects.get_upcoming_birthdays()
#     birthdays_today = Contact.objects.objects.get_birthdays()
#
#     context = {'birthday_today': birthday_today, 'birthday_upcoming': birthday_upcoming}
#     return render(request, 'contacts/contact_profile.html', context)

