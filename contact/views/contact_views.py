"""Module providing a function views."""
from django.shortcuts import render, get_object_or_404
from contact.models import Contact

# Create your views here.
def index(request):
    """Function rendering the index page."""
    contacts = Contact.objects.all()
    context = {
        'contacts': contacts,
    }
    return render(
        request,
        'contact/index.html',
        context
        )

def contact(request,contact_id):
    # one_contact = Contact.objects.filter(pk=contact_id).first()
    one_contact = get_object_or_404(Contact, pk=contact_id)
    #one_contact = get_object_or_404(Contact.objects.filter(pk=contact_id))
    context = {
        'contact': one_contact,
    }
    return render(
        request,
        'contact/contact.html',
        context
        )

