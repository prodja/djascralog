#! coding: utf-8
from django.shortcuts import render
from elasticsearch import Elasticsearch
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf

def spider(request):
	context={}	
	context['spider']=1
	
	if request.POST and request.POST.get('search','')!='':
		search=request.POST.get('search','')
		
		es = Elasticsearch(hosts=[{'host': 'localhost', 'port': 9200}])
		qdsl={'fields': ['name', 'code','url'], 'query': {'match': {'name': search}}}
		qcount={'query': {'match': {'name': search}}}
		res=es.search(index='gearbest_index',doc_type='product_type', body=qdsl,size=5000)
		cnt=es.count(index='gearbest_index',doc_type='product_type', body=qcount)
		if(res):
			res=res['hits']['hits']
			context['message']="Результаты по '"+str(search)+"'. Найдено: "+str(len(res))+" cnt="+str(cnt['count'])
			context['finded']=[]
			for rs in res:
				val = rs['fields']
				# val=[ rs['fields']['code'][0], rs['fields']['name'][0], rs['fields']['url'][0] ]
				context['finded'].append(val)

	if(request.POST.get('reset','')):
		context['message']=''

	return render_to_response('spider.html',context, context_instance=RequestContext(request))

