#! coding: utf-8

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html 
from json import dumps
from elasticsearch import Elasticsearch

class DjspiderPipeline(object):
    def process_item(self, item, spider):
      
      # import pdb; pdb.set_trace()
      es = Elasticsearch(hosts=[{'host': 'localhost', 'port': 9200}])
      if(es.exists(index="gearbest_index",doc_type='product_type',id=item['code'])):
        print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        print str(item['code'])+' - exist'      
        
      else:
        item = dict(item)        
        es.index(index="gearbest_index",doc_type='product_type', body=item, id=item['code'])
      return item
