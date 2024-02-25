from django.urls import path
from . import views

urlpatterns = [
    # Wird http://127.0.0.1 aufgerufen, so soll eine HTML Seite
    # namens home.html geladen werden
    # hierzu muss eine View erstellt werden und eine HTML Datei
    # namens home.html
    path('', views.home, name='home'),
]

