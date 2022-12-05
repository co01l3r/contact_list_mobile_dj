from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from django.shortcuts import redirect, reverse
from .models import Contact
import datetime
from django.http import HttpResponseRedirect
from django.utils import timezone
from datetime import timedelta


# Create your views here.
def index(request):
    search_input = request.GET.get('search-area')

    datetime_now = timezone.now()
    birthdays_today = Contact.objects.all().filter(birthday__day=datetime_now.day, birthday__month=datetime_now.month)

    if search_input:
        contacts = Contact.objects.filter(name__icontains=search_input)
    else:
        contacts = Contact.objects.all()

    context = {'contacts': contacts, 'search_input': search_input, 'birthdays_today': birthdays_today}
    return render(request, 'index.html', context)


def add_contact(request):
    form = ContactForm()

    if request.method == 'POST':

        print(request.POST)

        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact added')
            return HttpResponseRedirect('/')
        else:
            messages.error(request, 'Invalid credentials')

    context = {'form': form}
    return render(request, 'contacts/contact_form.html', context)


def contact_details(request, pk):
    contact = Contact.objects.get(id=pk)

    context = {'contact': contact}
    return render(request, 'contacts/contact_details.html', context)


def contact_update(request, pk):
    contact = Contact.objects.get(id=pk)
    form = ContactForm(request.POST or None, instance=contact)

    if request.method == 'POST':

        print(request.POST)

        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact updated')
            return HttpResponseRedirect('/')
        else:
            form = ContactForm(instance=contact)
            messages.error(request, 'Invalid credentials')

    context = {'form': form, 'contact': contact}
    return render(request, 'contacts/contact_form.html', context)


def contact_delete(request, pk):
    contact = Contact.objects.get(id=pk)

    if request.method == 'POST':
        contact.delete()
        messages.success(request, 'Contact deleted')
        return HttpResponseRedirect('/')


