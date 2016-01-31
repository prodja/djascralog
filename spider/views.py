#! coding: utf-8
from django.shortcuts import render
from elasticsearch import Elasticsearch
from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf

def spider(request):
	args={}
	args.update(csrf(request))
	args['spider']=1
	search=request.POST.get('search','')
	if request.POST:
		es = Elasticsearch(hosts=[{'host': 'localhost', 'port': 9200}])
		#qdsl={"match":{"name" : search}}
		qdsl="http://localhost:9200/gearbest_index/product_type/_search?q=name:"+str(search)
		args['message']="Результаты по '"+str(search)+"':"
		res=es.search(index='gearbest_index',doc_type='product_type',body=qdsl)
		args['message']+=type(res)

	return render_to_response('spider.html',args)

