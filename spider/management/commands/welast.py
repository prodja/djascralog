#! coding=utf-8
from django.core.management.base import BaseCommand
from elasticsearch import Elasticsearch
from json import loads 
import re
#import pdb; pdb.set_trace()
class Command(BaseCommand):

	def handle(self, *args, **options):

		es = Elasticsearch(hosts=[{'host': 'localhost', 'port': 9200}])
		fop=open('spider/management/commands/items.txt', 'r')
		r=str(fop.read())
		#r="{u'_type': u'GearBestItem', u'code': u'132992601', u'name': u'G1W-CB Full Black 2.7 inch 1080P Full HD Car DVR 5.0MP Resolution 4X Digital Zoom Video Recorder 120 Degree Wide Angle Lens with Charger  (Capacitor Battery)', u'img': u'http://gloimg.gearbest.com/gb/2015/201506/goods-img/1433815949936-P-2714228.jpg', u'_key': u'34190/1/8/0', u'url': u'http://www.gearbest.com/car-dvr/pp_196898.html', u'price_reg': [u'85.63'], u'price_discount': [u'41.64']}"
		list_jsons=[]
		r=r.replace("u'", '"')
		r=r.replace("'", '"')
		arr_json=re.findall("{.*}",r)
		for jsonline in arr_json:
			jobj=loads(jsonline)
			if(es.exists(index="gearbest_index",doc_type='product_type',id=jobj['code'])):
				get_doc=es.get(index="gearbest_index",doc_type='product_type',id=jobj['code'],_source=True)
				list_of_fieds=['price_reg','price_discount']
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
