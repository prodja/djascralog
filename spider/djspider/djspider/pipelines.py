#! coding: utf-8

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html 
from json import dumps
from elasticsearch import Elasticsearch

class DjspiderPipeline(object):
    def process_item(self, item, spider):
    	es = Elasticsearch(hosts=[{'host': 'localhost', 'port': 9200}])
    	if(es.exists(index="gearbest_index",doc_type='product_type',id=item['code'])):
    		print str(item['code'])+' - exist'

        return item

        """
        Traceback (most recent call last):
  File "/home/faa/.virtualenvs/django_1_8_5/local/lib/python2.7/site-packages/twisted/internet/defer.py", line 588, in _runCallbacks
    current.result = callback(current.result, *args, **kw)
  File "/home/faa/.virtualenvs/django_1_8_5/bin/firstapp/spider/djspider/djspider/pipelines.py", line 13, in process_item
    if(es.exists(index="gearbest_index",doc_type='product_type',id=item['code'])):
  File "/home/faa/.virtualenvs/django_1_8_5/local/lib/python2.7/site-packages/elasticsearch/client/utils.py", line 65, in _wrapped
    return func(*args, params=params, **kwargs)
  File "/home/faa/.virtualenvs/django_1_8_5/local/lib/python2.7/site-packages/elasticsearch/client/__init__.py", line 167, in exists
    self.transport.perform_request('HEAD', _make_path(index, doc_type, id), params=params)
  File "/home/faa/.virtualenvs/django_1_8_5/local/lib/python2.7/site-packages/elasticsearch/transport.py", line 217, in perform_request
    status, raw_data = connection.perform_request(method, url, params, body)
  File "/home/faa/.virtualenvs/django_1_8_5/local/lib/python2.7/site-packages/elasticsearch/connection/http.py", line 69, in perform_request
    self._raise_error(response.status, raw_data)
  File "/home/faa/.virtualenvs/django_1_8_5/local/lib/python2.7/site-packages/elasticsearch/connection/base.py", line 82, in _raise_error
    raise HTTP_EXCEPTIONS.get(status_code, TransportError)(status_code, error_message, additional_info)
TransportError: TransportError(400, u'')

        """
