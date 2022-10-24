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
#done
class FieldMissionsViewList(ListView):
    paginate_by = 20
    model = FieldMissionsView

# done
class FormationsViewList(ListView):
    paginate_by = 50
    model = FormationsView


class GeographyColumnsViewList(ListView):
    paginate_by = 50
    model = GeographyColumnsView


class AnalysisArArViewList(ListView):
    paginate_by = 50
    model = AnalysisArArView


class AnalysisFissionTracksViewList(ListView):
    paginate_by = 50
    model = AnalysisFissionTracksView


class ContactsViewList(ListView):
    paginate_by = 50
    model = ContactsView


class AnalysisUHeViewList(ListView):
    paginate_by = 50
    model = AnalysisUHeView


class FieldMissionsViewList(ListView):
    paginate_by = 50
    model = FieldMissionsView


class GeometryColumnsViewList(ListView):
    paginate_by = 50
    model = GeometryColumnsView


class LithologyDescriptionViewList(ListView):
    paginate_by = 50
    model = LithologyDescriptionView


class MeasurementsLinesViewList(ListView):
    paginate_by = 50
    model = MeasurementsLinesView


class MeasurementsPlanesViewList(ListView):
    paginate_by = 50
    model = MeasurementsPlanesView


class MissionsViewList(ListView):
    paginate_by = 50
    model = MissionsView


class SampleSectionsViewList(ListView):
    paginate_by = 50
    model = SampleSectionsView


class SamplesViewList(ListView):
    paginate_by = 50
    model = SamplesView

