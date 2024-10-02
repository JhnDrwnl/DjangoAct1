from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Logitrack'),
    path('trackOrder', views.trackOrder, name='trackOrder'),
    path('about', views.about, name='about')
]
