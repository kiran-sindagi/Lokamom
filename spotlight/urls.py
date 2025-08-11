from django.urls import path
from .views import WomenInSpotlight_list # This line is commented out

urlpatterns = [
    path('', WomenInSpotlight_list, name='WISList'),
]