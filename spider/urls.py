from django.conf.urls import include, url


urlpatterns = [
			url(r'^', 'spider.views.spider'),
			url(r'^/(?P<page>\d+)/(?P<zap>\d+)$','spider.views.spider'),
]

