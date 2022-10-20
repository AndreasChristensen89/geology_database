from django.urls import path
from . import views

app_name = 'INTERFACE'

urlpatterns = [
    path('', views.index, name='index'),
    path('samples-model', views.SamplesListView.as_view(), name='sample_model'),
    path('contacts-model', views.ContactsListView.as_view(), name='contacts_model'),
    path('lexicon-follies-model', views.LexiconFossilsListView.as_view(), name='lexicon_follies_model'),
]