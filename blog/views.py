from django.views.generic import *
from blog.models import *
from django.db.models import *

class PostsView(DetailView):
    
    queryset = Posts.objects.all() 

    template_name = 'articles.html'

    slug_field = 'slug'

    slug_url_kwarg = 'slug'

    context_object_name = 'article'
