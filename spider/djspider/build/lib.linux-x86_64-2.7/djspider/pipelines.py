#! coding: utf-8

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html 
from elasticsearch import Elasticsearch

class DjspiderPipeline(object):
    """def process_item(self, item, spider):

      # import pdb; pdb.set_trace()
      es = Elasticsearch(hosts=[{'host': 'localhost', 'port': 9200}])
      if(es.exists(index="gearbest_index",doc_type='product_type',id=item['code'])):
        get_doc=es.get(index="gearbest_index",doc_type='product_type',id=item['code'],_source=True)
        list_of_fieds=['price_reg','price_discount']
        for lf in list_of_fieds:
          if lf in item and len(item[lf])>0:
            last_item=unicode(item[lf][0])
            try:
              if len(get_doc['_source'][lf])>0:
                nl=[]
                if(type(get_doc['_source'][lf])==list):
                  nl=get_doc['_source'][lf]
                elif(type(get_doc['_source'][lf])==unicode):
                  nl.append(get_doc['_source'][lf]) 
                nl.append(last_item)
                item[lf]=nl
            except TypeError:
              import pdb; pdb.set_trace()
              print '()()(()()()()(()()()TypeError='+item['code']

      item = dict(item)        
      es.index(index="gearbest_index",doc_type='product_type', body=item, id=item['code'])
      return item"""
