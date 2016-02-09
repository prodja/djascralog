#! coding: utf-8
from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from re import match
from forms import SearchForm
from django.core.paginator import Paginator
from fns import sel_from_elast

def spider(request,page=1,zap_from_get=''):
	context={}	
	context['spider']=1
	hits_count=7

	if request.method == 'POST':

		context['search_form'] = SearchForm(request.POST)

		if context['search_form'].is_valid():

			find=context['search_form'].cleaned_data['search']

			if len(find)>1:
				
				find=find.encode('utf-8')
				find=find.lower()
				find=find.strip('*./:,?!+-=&?\'"')

				context['curpage']=page
				context['zap_from_get']=find
				context=dict(context.items()+sel_from_elast(find,['name', 'code','url'],'gearbest_index','product_type',hits_count,page-1).items())
			
			else:
				context['message']='Введите в поиск корректную строку (более одного символа)'		

	else: 
		context['search_form'] = SearchForm()
		if zap_from_get!='':
			context['search_form'] = SearchForm({'search':zap_from_get})
			context['zap_from_get']=zap_from_get
			context=dict(context.items()+sel_from_elast(zap_from_get,['name', 'code','url'],'gearbest_index','product_type',hits_count,int(page)-1).items())
			context['search_form'] = SearchForm()


	return render_to_response('spider.html',context, context_instance=RequestContext(request))

