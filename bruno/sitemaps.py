from django.contrib.sitemaps import Sitemap
from blog.models import Posts

class PostsSitemaps(Sitemap):
    
    def items(self):
        return Posts.objects.all()