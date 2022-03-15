from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap
from .feeds import LatestPostsFeed
sitemaps = {
 'posts': PostSitemap,
}
app_name='blog'

urlpatterns=[
#post views
path('',views.post_list,name='post_list'),
path('<int:year>/<int:month>/<int:day>/<slug:post>/',
views.post_detail,name='post_detail'),
path('<int:post_id>/share/',
 views.post_share, name='post_share'),
 path('sitemaps/', sitemap, {'sitemaps': sitemaps},
 name='django.contrib.sitemaps.views.sitemap'),
 path('feed/', LatestPostsFeed(), name='post_feed')
]
