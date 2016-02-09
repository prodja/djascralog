#! coding: utf-8
from elasticsearch import Elasticsearch

def sel_from_elast(find='',fields=[],index_doc='gearbest_index',doctype='product_type',size_s=10,form_s=0):

	"""Запрос в эластик"""
	es = Elasticsearch(hosts=[{'host': 'localhost', 'port': 9200}])
	qdsl={'fields': fields, 'query': {'match': {'_all': find}}}
	res=es.search(index=index_doc,doc_type=doctype, body=qdsl,size=size_s,from_=form_s)
	out_dict={}

	"""Вычисляем количество страниц """
	total=res['hits']['total']
	tmp=total/size_s
	out_dict['page_count']=round(tmp+0.5)

	"""и генерируем список страниц"""
	out_dict['pages']=[x for x in range(1,int(out_dict['page_count']))]

	"""Заполняем результатами выходной словарь"""
	res=res['hits']['hits']
	out_dict['finded']=[]
	for rs in res:
		val = rs['fields']
		out_dict['finded'].append(val)

	return out_dict