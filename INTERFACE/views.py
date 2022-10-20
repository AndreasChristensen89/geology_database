from django.shortcuts import render
from .models import Samples, AnalysisAr, AnalysisFt
from django.views.generic import ListView

def index(request):
    template = "INTERFACE/index.html"

    return render(request, template)

class SamplesListView(ListView):
    paginate_by = 50
    model = Samples

class AnalysisArListView(ListView):
    paginate_by = 50
    model = AnalysisAr

class AnalysisFtListView(ListView):
    paginate_by = 50
    model = AnalysisFt
