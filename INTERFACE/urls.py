from django.urls import path
from . import views

app_name = 'INTERFACE'

urlpatterns = [
    path('', views.index, name='index'),
    path('samples-model', views.SamplesListView.as_view(), name='sample_model'),
    path('contacts-model', views.ContactsListView.as_view(), name='contacts_model'),
    path('lexicon-follies-model', views.LexiconFossilsListView.as_view(), name='lexicon_follies_model'),
    path('field-missions-view', views.FieldMissionsViewList.as_view(), name='field_missions_view'),
    # Postgres views
    path('field-missions-view', views.FieldMissionsViewList.as_view(), name='field_missions_view'),
    path('formation-view', views.FormationsViewList.as_view(), name='formation_view'),
    path('geography-columns-view', views.GeographyColumnsViewList.as_view(), name='geography_columns_view'),
    path('analysis-ar-ar-view', views.AnalysisArArViewList.as_view(), name='analysis_ar_ar_view'),
    path('analysis-fission-tracks-view', views.AnalysisFissionTracksViewList.as_view(), name='analysis_fission_tracks_view'),
    path('contacts-view', views.ContactsViewList.as_view(), name='contacts_view'),
    path('analysis-UHe-view', views.AnalysisUHeViewList.as_view(), name='analysis_UHe_view'),
    path('field-mission-view', views.FieldMissionsViewList.as_view(), name='field_mission_view'),
    path('geometry-columns-view', views.GeometryColumnsViewList.as_view(), name='geometry_columns_view'),
    path('lithology-description-view', views.LithologyDescriptionViewList.as_view(), name='lithology_description_view'),
    path('location-view', views.LocaltionViewList.as_view(), name='location_view'),
    path('measurements-lines-view', views.MeasurementsLinesViewList.as_view(), name='measurements_lines_view'),
    path('measurements-planes-view', views.MeasurementsPlanesViewList.as_view(), name='measurements_planes_view'),
    path('missions-view', views.MissionsViewList.as_view(), name='missions_view'),
    path('sample-sections-view', views.SampleSectionsViewList.as_view(), name='sample_sections_view'),
    path('samples-view', views.SamplesViewList.as_view(), name='samples_view'),
]