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
            messages.success(request, 'Contact added')
            # return redirect(request, 'index')
        else:
            form = ContactForm(instance=contact)

    context = {'form': form}
    return render(request, 'contacts/contact_form.html', context)


