from django.shortcuts import render

def home(request):
    # home.html aus dem Template Verzeichnis laden.
    # home.html muss noch erstellt werden
    return render(request, 'home.html')