from django.shortcuts import render
from articles.views import random_articles 


# Create your views here.
def home(request):
    article_data = random_articles()
    return render(request, 'animated.html', {"article_data":article_data})

def about(request):
    return render(request, 'about.html')

