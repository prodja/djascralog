#! coding=utf-8
from django.core.management.base import BaseCommand
from elasticsearch import Elasticsearch
from elasticsearch.client import IndicesClient
from json import loads 
from sys import argv
#import pdb; pdb.set_trace()
class Command(BaseCommand):

	def handle(self, *args, **options):

		es = Elasticsearch(hosts=[{'host': 'localhost', 'port': 9200}])

		fop=open('spider/management/commands/'+str(argv[2]), 'r')
		inds = IndicesClient(es)

		mapping={ "mappings": { "product_type":  {  "properties": { "code": { "type" : "string" },"name": {"type" : "string"},"img": {"type" : "string"},"url": {"type" : "string"},"price_reg": {"type" : "float"},"price_discount": {"type" : "float"}}}}}

		if(inds.exists(index='gearbest_index')):
			print 'gearbest_index exist'
		else:
			inds.create(index='gearbest_index',body=mapping)
			print 'gearbest_index created'

		for jsonline in fop:
			jobj=loads(jsonline)
			del jobj["_type"]
			es.index(index="gearbest_index",doc_type='product_type', body=jobj, id=jobj['code'])

	def add_arguments(self, parser):
		
		parser.add_argument('file', nargs='+')

