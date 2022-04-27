from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('inventory/<str:station_id>/', views.station_detail, name='station_detail'),
    path('history/<str:station_id>/', views.station_history, name='station_history'),
    path('instrument/<int:equipment_pk>/', views.instrument_detail, name='instrument_detail'),
]