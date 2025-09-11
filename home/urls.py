from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contribute/', views.contribute, name='contribute'),
    path('successful/', views.successful, name='successful'),
    path('work-career/', views.workCareer, name = "work-career")
]
