#! coding: utf-8
from django.shortcuts import render
from elasticsearch import Elasticsearch
from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf

def spider(request):
	args={}
	args.update(csrf(request))
	args['spider']=1
	
	if request.POST and request.POST.get('search','')!='':
		search=request.POST.get('search','')
		es = Elasticsearch(hosts=[{'host': 'localhost', 'port': 9200}])
		qdsl={'fields': ['name', 'code'], 'query': {'match': {'name': search}}}
		res=es.search(index='gearbest_index',body=qdsl)
		if(res):
			args['message']="Результаты по '"+str(search)+"':\n"
			print res

			res=res['hits']['hits']
			args['finded']=[]

			for rs in res:
				val=[rs['fields']['code'][0],rs['fields']['name'][0]]
				args['finded'].append(val)

		
	if(request.POST.get('reset','')):
		args['message']=''

	return render_to_response('spider.html',args)

