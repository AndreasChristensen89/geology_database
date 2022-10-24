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
# done
class FieldMissionsViewList(ListView):
    paginate_by = 20
    model = FieldMissionsView

# done
class FormationsViewList(ListView):
    paginate_by = 50
    model = FormationsView

# not used for now
class GeographyColumnsViewList(ListView):
    paginate_by = 50
    model = GeographyColumnsView

# done
class AnalysisArArViewList(ListView):
    paginate_by = 50
    model = AnalysisArArView

# done
class AnalysisFissionTracksViewList(ListView):
    paginate_by = 50
    model = AnalysisFissionTracksView

# done
class ContactsViewList(ListView):
    paginate_by = 50
    model = ContactsView

# done
class AnalysisUHeViewList(ListView):
    paginate_by = 50
    model = AnalysisUHeView

# done
class FieldMissionsViewList(ListView):
    paginate_by = 50
    model = FieldMissionsView

# not for now
class GeometryColumnsViewList(ListView):
    paginate_by = 50
    model = GeometryColumnsView

# done
class LithologyDescriptionViewList(ListView):
    paginate_by = 50
    model = LithologyDescriptionView

# done
class LocaltionViewList(ListView):
    paginate_by = 50
    model = LocationsView

# done
class MeasurementsLinesViewList(ListView):
    paginate_by = 50
    model = MeasurementsLinesView

# done
class MeasurementsPlanesViewList(ListView):
    paginate_by = 50
    model = MeasurementsPlanesView

# done
class MissionsViewList(ListView):
    paginate_by = 50
    model = MissionsView

# done
class SampleSectionsViewList(ListView):
    paginate_by = 50
    model = SampleSectionsView

# done
class SamplesViewList(ListView):
    paginate_by = 50
    model = SamplesView

