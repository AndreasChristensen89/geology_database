from django.urls import path
from . import views

app_name = 'INTERFACE'

urlpatterns = [
    path('', views.index, name='index'),
    path('data-display', views.data_display, name='data_display')
]