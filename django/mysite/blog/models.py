from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django.core.urlresolvers import reverse

from taggit.managers import TaggableManager
    
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User,
                                related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                                choices=STATUS_CHOICES,
                                default='draft')
    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.

    tags = TaggableManager()


    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',
            args=[self.publish.year,
                self.publish.strftime('%m'),
                self.publish.strftime('%d'),
                self.slug])

#    def remove(self, comment):
        """
        Remove a comment from the post.
        """
#        comment_id = str(comment.id)   
#        if comment_id in self.post:     
#            del self.post[comment_id]
#            self.save()



class Comment(models.Model):
    """docstring for Comment"""
    post = models.ForeignKey(Post , related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        """docstring for Meta"""
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)


 





    