from django.urls import path
from . import views

urlpatterns = [
    path('', views.Letter, name="letter"),
    path('what-we-offer/', views.whatWeOffer, name="session"),
    path("one-on-one/", views.oneOnOne, name="one"),
    path("group-sessions/", views.groupSession, name="group"),
    path("stress-management", views.StressSession, name="stress")
]
