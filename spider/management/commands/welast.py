#! coding=utf-8
from django.core.management.base import BaseCommand
from elasticsearch import Elasticsearch
from elasticsearch.client import IndicesClient
from json import loads 
from sys import argv
from spider.models import Price_gb
from django.db import connection
from datetime import datetime
#import pdb; pdb.set_trace()
class Command(BaseCommand):

	def handle(self, *args, **options):

		es = Elasticsearch(hosts=[{'host': 'localhost', 'port': 9200}])

		fop=open('spider/management/commands/'+str(argv[2]), 'r')
		inds = IndicesClient(es)

		mapping={ "mappings": { "product_type":  {  "properties": { "code": { "type" : "string" },"name": {"type" : "string"},"img": {"type" : "string"},"url": {"type" : "string"},"price_reg": {"type" : "float"},"price_discount": {"type" : "float"}}}}}

		if not inds.exists(index='gearbest_index'):
			inds.create(index='gearbest_index',body=mapping)
			print 'gearbest_index created'

		for jsonline in fop:
			jobj=loads(jsonline)
			del jobj["_type"]
			#es.index(index="gearbest_index",doc_type='product_type', body=jobj, id=jobj['code'])
			
			disc=0
			reg=0

			if len(jobj['price_discount'])>0:
				disc  = float(jobj['price_discount'][0])
			if len(jobj['price_reg'])>0:
				reg  = float(jobj['price_reg'][0])

			#insert="INSERT into 'price_gb' ('price','price_disc','code','date') values ("+str(reg)+", "+str(disc)+", '"+str(jobj['code'])+"', '"+str(datetime.today())+"')"
			#cursor = connection.cursor()
			#cursor.execute(insert)

			add_price=Price_gb(price=reg,price_disc=disc,code=str(jobj['code']))
			add_price.save()

			print 'code='+str(jobj['code'])
	
	def add_arguments(self, parser):
		
		parser.add_argument('file', nargs='+')

