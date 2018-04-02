from django.contrib.sitemaps import Sitemap
from .models import Post


class PostSitemap(Sitemap):
    """docstring for PostSitemap"""
    changefreq = 'weekly'
    priorty = 0.9
    def items(self):
        return Post.published.all()
    def lastmod(self,obj):
        return obj.publish
        