from django.shortcuts import render, redirect
from .forms import ContactForm


# Create your views here.
def index(request):
    return render(request, 'index.html')


def add_contact(request):
    form = ContactForm()

    if request.method == 'POST':
        print(request.POST)
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'contacts/contact_form.html', context)
