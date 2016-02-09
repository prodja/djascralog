#! coding: utf-8
from elasticsearch import Elasticsearch

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
	for rs in res:
		val = rs['fields']
		finded.append(val)
	print 'pgs='+ str(pages)
	return finded, pages, page_count,