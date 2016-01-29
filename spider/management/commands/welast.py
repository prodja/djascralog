#! coding=utf-8
from django.core.management.base import BaseCommand
from elasticsearch import Elasticsearch
from elasticsearch.client import IndicesClient
from json import loads 
import re
#import pdb; pdb.set_trace()
class Command(BaseCommand):

	def handle(self, *args, **options):

		es = Elasticsearch(hosts=[{'host': 'localhost', 'port': 9200}])
		fop=open('spider/management/commands/items_gearbest_8.jl', 'r')
		inds = IndicesClient(es)

		mapping='{ "mappings": { "product_type":  {  "properties": { "code": { "type" : "string" },"name": {"type" : "string"},"img": {"type" : "string"},"url": {"type" : "string"},"price_reg": {"type" : "float"},"price_discount": {"type" : "float"}}}}}'

		if(inds.exists(index='gearbest_index')):
			print 'gearbest_index exist'
		else:
			inds.create(index='gearbest_index',body=mapping)
			print 'gearbest_index created'

		for jsonline in fop:
			jobj=loads(jsonline)
			jobj.pop("_type")
			import pdb; pdb.set_trace()
			if(es.exists(index="gearbest_index",doc_type='product_type',id=jobj['code'])):
				get_doc=es.get(index="gearbest_index",doc_type='product_type',id=jobj['code'],_source=True)
				list_of_fieds=['price_reg','price_discount']
				for lf in list_of_fieds:
					if lf in jobj and len(jobj[lf])>0:
						last_item=unicode(jobj[lf][0])
						try:
							if len(get_doc['_source'][lf])>0:
								nl=[]
							if(type(get_doc['_source'][lf])==list):
								nl=get_doc['_source'][lf]
							elif(type(get_doc['_source'][lf])==unicode):
								nl.append(get_doc['_source'][lf]) 
							nl.append(last_item)
							jobj[lf]=nl
						except TypeError:
							import pdb; pdb.set_trace()
							print '()()(()()()()(()()()TypeError='+jobj['code']

			jobj = dict(jobj)        
			es.index(index="gearbest_index",doc_type='product_type', body=jobj, id=jobj['code'])

