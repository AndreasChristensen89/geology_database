from django.shortcuts import render
from .models import Samples

def index(request):
    template = "INTERFACE/index.html"

    return render(request, template)


def data_display(request):

    samples = Samples.objects.all()
    template = 'INTERFACE/data_display.html'
    context = {
        "samples": samples
    }

    return render(request, template, context)
