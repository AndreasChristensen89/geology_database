# """Markers API views."""
# from rest_framework import viewsets
# from rest_framework_gis import filters

# from .models import LocationsView
# from .serializers import MarkerSerializer


# class MarkerViewSet(viewsets.ReadOnlyModelViewSet):
#     """Marker view set."""

#     bbox_filter_field = "location"
#     filter_backends = (filters.InBBoxFilter,)
#     queryset = LocationsView.objects.all()
#     serializer_class = MarkerSerializer