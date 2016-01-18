#! coding: utf-8
from elasticsearch import Elasticsearch
import httplib2
from os import getcwd
#test elastic in python
#товар - распарсил, в json -> (если _source пуст)документ elastic - заполняем _source в доке
#https://elasticsearch-py.readthedocs.org/en/master/api.html
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
doc='{"name":"one_name", "arrs":{"el1":1,"els2":2}}'
#res = es.index(index="gearbest_index", doc_type='product_type', id=5, body=doc)
#res=es.create(index="gearbest_index",doc_type='product_type',body=doc,id=1)
b=es.exists(index="gearbest_index",doc_type="product_type",id=1)
if(b==True):
	print 'OK'