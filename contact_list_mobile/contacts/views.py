from django.shortcuts import render, redirect
from .models import Contact


# Create your views here.
def index(request):
    return render(request, 'index.html')


def add_contact(request):
    if request.method == 'POST':
        new_contact = Contact(
            name=request.POST['name'],
            phone=request.POST['phone'],
            email=request.POST['email'],
            web=request.POST['web'],
            birthday=request.POST['birthday'],
            note=request.POST['note'],
        )
        new_contact.save()
    return render(request, 'contacts/edit_contact.html')

    # form = ContactForm()
    #
    # if request.method == 'POST':
    #     form = ContactForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #
    # context = {'form': form}
    # return render(request, 'contacts/edit_contact.html')
