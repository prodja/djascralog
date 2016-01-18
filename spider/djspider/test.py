#! coding: utf-8
from elasticsearch import Elasticsearch
import httplib2
from os import getcwd

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
doc='{"name":"one_name", "arrs":{"el1":1,"els2":2}}'
res = es.index(index="gearbest_index", doc_type='product_type', id=5, body=doc)