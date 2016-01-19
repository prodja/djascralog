#! coding: utf-8

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html 
from json import dumps
from elasticsearch import Elasticsearch

class DjspiderPipeline(object):
    def process_item(self, item, spider):
    	line = dumps(dict(item))
    	es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    	res=es.create(index="gearbest_index",doc_type='product_type',body=line, id=item['code'])
    	print 'code='+str(item['code'])
        return item
