from django.shortcuts import render

def index(request):
    template = "INTERFACE/index.html"

    return render(request, template)
