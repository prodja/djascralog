#! coding: utf-8
from django.template import RequestContext
from django.shortcuts import render_to_response
from forms import SearchForm
from fns import sel_from_elast

def spider(request,page=1,zap_from_get=''):
	context={}	
	context['spider']=1
	""" кол-во выводимых товаров на одной странице (size)"""
	hits_count=7

	""" Если запрос пришел из формы """
	if request.method == 'POST':

		context['search_form'] = SearchForm(request.POST)

		""" Проверка пришедшего с формы и его подготовка к запросу в эластик """
		if context['search_form'].is_valid():

			find=context['search_form'].cleaned_data['search']

			if len(find)>1:
				
				find=find.encode('utf-8')
				find=find.lower()
				find=find.strip('*./:,?!+-=&?\'"')

				context['curpage']=page
				context['zap_from_get']=find

				""" Запрос в эластик и получение товаров """
				context=dict(context.items()+sel_from_elast(find,['name', 'code','url'],'gearbest_index','product_type',hits_count,page-1).items())
			
			else:
				context['message']='Введите в поиск корректную строку (более одного символа)'		

	else:
		""" Если запрос пришел с url'а (с постраничника) """ 
		context['search_form'] = SearchForm()

		""" Если с постраничника пришел текст запроса с формы """ 
		if zap_from_get!='':

			context['search_form'] = SearchForm({'search':zap_from_get})
			context['zap_from_get']=zap_from_get

			""" Делаем запрос в эластик и получаем товары """
			context=dict(context.items()+sel_from_elast(zap_from_get,['name', 'code','url'],'gearbest_index','product_type',hits_count,int(page)-1).items())
			context['search_form'] = SearchForm()


	return render_to_response('spider.html',context, context_instance=RequestContext(request))

