from re import template
from django.shortcuts import render
from .models import *
from django.views.generic import ListView

def index(request):
    template = "INTERFACE/index.html"

    return render(request, template)

class SamplesListView(ListView):
    paginate_by = 20
    model = Samples

class ContactsListView(ListView):
    paginate_by = 20
    model = Contacts

class LexiconFossilsListView(ListView):
    paginate_by = 20
    model = LexiconFossils

# -------------------------------------- views --------------------------------------

class FieldMissionsViewList(ListView):
    paginate_by = 20
    model = FieldMissionsView
