from django.urls import path
from .views import inicio, quienesSom, galeria, registro
from . import views

urlpatterns = [
    path('', inicio, name="inicio"),
    path('quienesSom/', quienesSom, name="quienesSom"),
    path('galeria/', galeria, name="galeria"),
    path('cerrar/', views.cerrar, name='cerrar'),
    path('registro/', registro, name="registro"),

]