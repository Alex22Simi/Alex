from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test, name='test'),
    path('aplicatie/', views.aplicatie, name='aplicatie'),
    path('adauga/', views.adugare_notite, name='adaugare_notite'),
    path('numar/',views.afisare_numar, name='afisare_numar'),
    path('rand/',views.afisare_notita, name='afisare_notite')
]
