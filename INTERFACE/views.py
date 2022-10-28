from re import template
from django.shortcuts import render
from .models import *
from django.views.generic import ListView
from django.core import serializers
import folium

def index(request):
    template = "INTERFACE/index.html"
    lat = 15
    lat_two = 10
    lng = -10
    lng_two = 50
    text = "Somewhere"
    text_two = "Somewhere Else"
    content = "Place"
    content_two = "Another Place"

    contacts = Contacts.objects.all()
    list = ""
    for obj in contacts:
        list = list + f'<p>{obj.contact_id}</p>'

    m = folium.Map(location=[19, -12], zoom_start=2)

    folium.Marker([lat, lng], tooltip=text, popup=content).add_to(m)
    folium.Marker([lat_two, lng_two], tooltip=text_two, popup=list).add_to(m)

    m = m._repr_html_()
    context = {
        'm': m
    }

    return render(request, template, context)

class SamplesListView(ListView):
    paginate_by = 20
    model = Samples

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['fields'] = [f.name for f in Samples._meta.get_fields()]
        return context

class ContactsListView(ListView):
    paginate_by = 20
    model = Contacts

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['fields'] = [f.name for f in Contacts._meta.get_fields()]
        return context

class LexiconFossilsListView(ListView):
    paginate_by = 20
    model = LexiconFossils

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['fields'] = [f.name for f in LexiconFossils._meta.get_fields()]
        return context

# -------------------------------------- views --------------------------------------
# done
class FieldMissionsViewList(ListView):
    paginate_by = 20
    model = FieldMissionsView

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['fields'] = [f.name for f in FieldMissionsView._meta.get_fields()]
        return context

# done
class FormationsViewList(ListView):
    paginate_by = 50
    model = FormationsView

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['fields'] = [f.name for f in FormationsView._meta.get_fields()]
        return context

# not used for now
# class GeographyColumnsViewList(ListView):
#     paginate_by = 50
#     model = GeographyColumnsView

#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super().get_context_data(**kwargs)
#         context['fields'] = [f.name for f in GeographyColumnsView._meta.get_fields()]
#         return context

# done
class AnalysisArArViewList(ListView):
    paginate_by = 50
    model = AnalysisArArView

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['fields'] = [f.name for f in AnalysisArArView._meta.get_fields()]
        return context

# base done
class AnalysisFissionTracksViewList(ListView):
    paginate_by = 50
    model = AnalysisFissionFracksView

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['fields'] = [f.name for f in AnalysisFissionFracksView._meta.get_fields()]
        return context

# base done
class ContactsViewList(ListView):
    paginate_by = 50
    model = ContactsView

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['fields'] = [f.name for f in ContactsView._meta.get_fields()]
        return context

# base done
class AnalysisUHeViewList(ListView):
    paginate_by = 50
    model = AnalysisUHeView

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['fields'] = [f.name for f in AnalysisUHeView._meta.get_fields()]
        return context

# base done
class FieldMissionsViewList(ListView):
    paginate_by = 50
    model = FieldMissionsView

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['fields'] = [f.name for f in FieldMissionsView._meta.get_fields()]
        return context

# not for now
class GeometryColumnsViewList(ListView):
    paginate_by = 50
    model = GeometryColumns

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['fields'] = [f.name for f in GeometryColumns._meta.get_fields()]
        return context

# base done
class LithologyDescriptionViewList(ListView):
    paginate_by = 50
    model = LithologyDescriptionView

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['fields'] = [f.name for f in LithologyDescriptionView._meta.get_fields()]
        return context

# base done
class LocaltionViewList(ListView):
    paginate_by = 50
    model = LocationsView

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['fields'] = [f.name for f in LocationsView._meta.get_fields()]
        return context

# base done
class MeasurementsLinesViewList(ListView):
    paginate_by = 50
    model = MeasurementsLinesView

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['fields'] = [f.name for f in MeasurementsLinesView._meta.get_fields()]
        return context

# base done
class MeasurementsPlanesViewList(ListView):
    paginate_by = 50
    model = MeasurementsPlanesView

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['fields'] = [f.name for f in MeasurementsPlanesView._meta.get_fields()]
        return context

# base done
class MissionsViewList(ListView):
    paginate_by = 50
    model = FieldMissionsView

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['fields'] = [f.name for f in FieldMissionsView._meta.get_fields()]
        return context

# base done
class SampleSectionsViewList(ListView):
    paginate_by = 50
    model = SampleSectionsView

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['fields'] = [f.name for f in SampleSectionsView._meta.get_fields()]
        return context

# base done
class SamplesViewList(ListView):
    paginate_by = 50
    model = SamplesView

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['fields'] = [f.name for f in SamplesView._meta.get_fields()]
        return context


def testFieldNames(request):
    data = serializers.serialize("python", SamplesView.objects.all())
    object = SamplesView.objects.all().first()

    template = "INTERFACE/test_fields.html"

    context = {
        "data": data,
        "object": object
    }

    return render(request, template, context)

def testFieldNamesNew(request):
    data = serializers.serialize("python", SamplesSections.objects.all())
    object = SamplesSections.objects.get(material_sample_id="ARe002")

    template = "INTERFACE/test_fields.html"

    context = {
        "data": data,
        "object": object
    }

    return render(request, template, context)