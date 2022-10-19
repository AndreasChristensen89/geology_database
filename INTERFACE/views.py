from django.shortcuts import render

def index(request):
    template = "INTERFACE/index.html"

    return render(request, template)


def data_display(request):
    template = 'INTERFACE/data_display.html'

    return render(request, template)
