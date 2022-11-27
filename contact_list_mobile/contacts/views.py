from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def add_contact(request):
    # form = ContactForm()
    #
    # if request.method == 'POST':
    #     form = ContactForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #
    # context = {'form': form}
    return render(request, 'contacts/edit_contact.html')
