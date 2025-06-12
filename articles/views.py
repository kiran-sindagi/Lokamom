from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Articles
from forums.models import Post

# Create your views here.
class ArticlesListView(ListView):
    model = Articles
    template_name = 'articles.html'
    paginate_by = 10
    context_object_name = "items"
    def get_queryset(self):
        return Articles.objects.all()

def readArticle(request, pk):
    article = get_object_or_404(Articles, pk=pk)
    import bleach
    allowed_tags = ['b', 'strong', 'i', 'em', 'br', 'p', 'span', 'a']
    article.body = bleach.clean(article.body, tags=allowed_tags)
    try:
        post = Post.objects.get(body=article.question)  # or slug=article.slug
    except Post.DoesNotExist:
        post = None
    return render(request, 'read.html', {
        'article': article,
        'post': post
    })
    
