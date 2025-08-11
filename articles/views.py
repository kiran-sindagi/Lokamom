from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView
from .models import Articles
from forums.models import Post
from django.db.models import Q
import random
import bleach

class SectionsView(TemplateView):
    template_name = 'sections.html'

class ArticlesListView(ListView):
    model = Articles
    template_name = 'articles.html'
    paginate_by = 10
    context_object_name = "items"

    def get_queryset(self):
        section = self.kwargs.get('section')
        return Articles.objects.filter(section=section)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = self.kwargs.get('section')
        return context

def readArticle(request, pk):
    article = get_object_or_404(Articles, pk=pk)
    allowed_tags = ['b', 'strong', 'i', 'em', 'br', 'p', 'span', 'a', 'big']
    article.body = bleach.clean(article.body, tags=allowed_tags)
    try:
        post = Post.objects.get(body=article.question)  # or slug=article.slug
    except Post.DoesNotExist:
        post = None
    return render(request, 'read.html', {
        'article': article,
        'post': post
    })

def random_articles():
    # Get all articles
    all_articles = Articles.objects.all()
    
    # Convert queryset to list and shuffle
    articles_list = list(all_articles)
    section_5 = random.choice(articles_list[0:5])
    section_4 = random.choice(articles_list[5:10])
    section_3 = random.choice(articles_list[10:15])
    section_2 = random.choice(articles_list[15:20])
    section_1 = random.choice(articles_list[20:25])
    random_articles = [section_1,section_2,section_3,section_4,section_5]
    # Prepare articles with truncated body
    articles_data = []
    for article in random_articles:
        articles_data.append({
            'id': article.id,
            'title': article.title,
            'preview': article.body[:100] + '...' if len(article.body) > 100 else article.body,
            'section': article.section
        })
    
    return articles_data

