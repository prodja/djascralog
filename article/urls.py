from django.conf.urls import include, url

urlpatterns = [
    url(r'^articles/get/(?P<article_id>\d+)/$', 'article.views.article'),
    url(r'^articles/addlike/(?P<article_id>\d+)/(?P<page_id>\d+)/$', 'article.views.addlike'),
    url(r'^articles/addcomment/(?P<article_id>\d+)/$', 'article.views.addcomment'),

    url(r'^articles/page/(?P<page_number>\d+)/$','article.views.articles'),

    url(r'^', 'article.views.articles'),
]
