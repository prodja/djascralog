from django.conf.urls import include, url


urlpatterns = [
			url(r'(?P<page>\d+)/(?P<zap_from_get>\w+)/$','spider.views.spider'),
			url(r'^$', 'spider.views.spider'),
]

