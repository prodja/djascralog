#! coding: utf-8
from spider.models import Price_gb
from elasticsearch import Elasticsearch
import datetime
from django.utils import timezone

def sel_from_elast(find='',fields=[], index_doc='gearbest_index',doctype='product_type',size_s=10,form_s=0):

	"""Запрос в эластик"""
	es = Elasticsearch(hosts=[{'host': 'localhost', 'port': 9200}])
	qdsl={'fields': fields, 'query': {'match': {'_all': find}}}
	res=es.search(index=index_doc,doc_type=doctype, body=qdsl,size=size_s,from_=form_s)
	

	"""Вычисляем количество страниц """
	total=res['hits']['total']
	tmp=total/size_s
	
	page_count=round(tmp+0.5)

	"""и генерируем список страниц"""
	pages=[x for x in range(1, int(page_count))]

	"""Заполняем результатами выходной словарь"""
	res=res['hits']['hits']
	finded =[]

	""" Заполняем список резалтами с эластика, делаем запрос в бд для списка цен """
	for rs in res:
		val = rs['fields']
		price_list=Price_gb.objects.filter(code__exact=val['code'][0])
		price_reg_list=[]
		price_discount_list=[]

		""" Если список пришедших с бд цен не пуст - добавляем его к выходному списку"""
		if(len(price_list)>0):
			for p in price_list:
				price_reg_list.append(p.price)
				price_discount_list.append(p.price_disc)

			val['price_reg_list']=price_reg_list
			val['price_discount_list']=price_discount_list

		finded.append(val)

	return finded, pages, page_count,