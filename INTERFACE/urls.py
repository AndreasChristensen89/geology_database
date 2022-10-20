from django.urls import path
from . import views

app_name = 'INTERFACE'

urlpatterns = [
    path('', views.index, name='index'),
    path('data-display', views.SamplesListView.as_view(), name='data_display')
]