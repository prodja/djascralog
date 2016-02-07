#! coding: utf-8
from django.shortcuts import render
from elasticsearch import Elasticsearch
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from re import match
from forms import SearchForm

def spider(request):
	context={}	
	context['spider']=1
	
	if request.method == 'POST':

		context['search_form'] = SearchForm(request.POST)

		if context['search_form'].is_valid():

			find=context['search_form'].cleaned_data['search']

			if len(find)>1:

				find=find.encode('utf-8')
				find=find.lower()
				find=find.strip('*./:,?!+-=&?\'"')
				res=''

				es = Elasticsearch(hosts=[{'host': 'localhost', 'port': 9200}])
				qdsl={'fields': ['name', 'code','url'], 'query': {'match': {'_all': find}}}
				res=es.search(index='gearbest_index',doc_type='product_type', body=qdsl,size=5000)

				if(res):
					res=res['hits']['hits']
					context['finded']=[]
					for rs in res:
						val = rs['fields']
						context['finded'].append(val)

				context['message']="Результаты по '"+str(find)+' ('+str(type(find))+") '. Найдено: "+str(len(res))

				return render_to_response('spider.html',context, context_instance=RequestContext(request))
				
			else:
				context['message']='Введите в поиск корректную строку (более одного символа)'		

	else: 
		context['message']=''
		context['search_form'] = SearchForm()

	return render_to_response('spider.html',context, context_instance=RequestContext(request))

