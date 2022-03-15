from django.db import models
from django.urls import reverse
# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class PublishedManager(models.Manager):
    """custom object manager for post object."""

    def get_queryset(self):
        return super(PublishedManager,self).get_queryset()\
                                            .filter(status='published')
class  Comment(models.Model):
    post= models.ForeignKey('Post', on_delete=models.CASCADE,
                                related_name='comments')
    name=models.CharField(max_length=80)
    email=models.EmailField()
    body= models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now_add=True)
    active= models.BooleanField(default=True)


    class Meta():
        ordering=('created',)

    def __str__(self):
        return f'comment by {self.name} on {self.post}'




class Post(models.Model):
    STATUS_CHOICES=(('draft','Draft'),
    ('published','Published'),)
    title= models.CharField(max_length=250)#create title
    slug= models.SlugField(max_length=250,
    unique_for_date='publish')#create url slug
    author= models.ForeignKey(User,on_delete=models.CASCADE,
    related_name='blog_posts')
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created= models.DateTimeField(auto_now_add=True)#date of post creation
    updated=models.DateTimeField(auto_now=True)#date of updating post
    status= models.CharField(max_length=10,
    choices= STATUS_CHOICES,default='draft')
    objects= models.Manager()#The default manager
    published=PublishedManager()# custom Manager
    def get_absolute_url(self):
         return reverse('blog:post_detail',
         args=[self.publish.year,
         self.publish.month,
        self.publish.day, self.slug])

    class Meta:
        ordering=('-publish',)

    def __str__(self):
        return self.title
