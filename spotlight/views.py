from django.shortcuts import render
from .models import WomenInSpotlight 

def WomenInSpotlight_list(request):
    """
    Renders a page displaying all WomenInSpotlights.
    """
    WomenInSpotlights = WomenInSpotlight.objects.all()
    return render(request, 'WomenInSpotlight_list.html', {'WomenInSpotlights': WomenInSpotlights})