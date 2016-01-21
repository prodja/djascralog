#! coding: utf-8

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html 
from elasticsearch import Elasticsearch

class DjspiderPipeline(object):
    def process_item(self, item, spider):

      # import pdb; pdb.set_trace()
      es = Elasticsearch(hosts=[{'host': 'localhost', 'port': 9200}])
      if(es.exists(index="gearbest_index",doc_type='product_type',id=item['code'])):
        print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        print str(item['code'])+' - exist'

        get_doc=es.get(index="gearbest_index",doc_type='product_type',id=item['code'],_source=True)
        list_of_fieds=['price_reg','price_discount']
        for lf in list_of_fieds:
          if lf in item and len(item[lf])>0:
            #import pdb; pdb.set_trace()
            if lf in get_doc['_source']:
              print  str(item['code']) + '*==*' + str(item[lf])
              print 'sc=' + str(get_doc['_source'])
              get_doc['_source'][lf]=list(get_doc['_source'][lf])
              #item[lf]=
              #i=type(get_doc['_source'][lf])
              import pdb; pdb.set_trace()
              new_list=list(get_doc['_source'][lf])

              i=new_list.append(str(item[lf]))

              print 'LLLLLLLLLLLLLLLLLLLLLLLLLLIiiiiist='+str(i)

      item = dict(item)        
      es.index(index="gearbest_index",doc_type='product_type', body=item, id=item['code'])
      return item
