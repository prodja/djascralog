#! coding: utf-8
from django.template import RequestContext
from django.shortcuts import render_to_response
from forms import SearchForm
from fns import sel_from_elast

def spider(request, page=1, zap_from_get=''):
	""" кол-во выводимых товаров на одной странице (size)"""
	hits_count=7
	
	spider_id=1
	curpage = 0
	items = None
	pages=[]
	page_count=0
	__fields = ['name', 'code', 'url']

	""" Если запрос пришел из формы """
	if request.POST:
		search_form = SearchForm(request.POST)

		""" Проверка пришедшего с формы и его подготовка к запросу в эластик """
		if search_form.is_valid():

			find=search_form.cleaned_data['search']			
			
			curpage = page
			zap_from_get = find

			""" Запрос в эластик и получение товаров """
			items, pages, page_count = sel_from_elast(find, __fields, size_s=hits_count, form_s=int(page)-1)
			
	else:
		
		""" Если запрос пришел с url'а (с постраничника) """ 
		search_form = SearchForm()

		""" Если с постраничника пришел текст запроса с формы """
		#if not zap_from_get:
		if zap_from_get:			
			search_form = SearchForm(initial={'search':zap_from_get})

			""" Делаем запрос в эластик и получаем товары """
			items, pages, page_count = sel_from_elast(zap_from_get, __fields, size_s=hits_count, form_s=int(page)-1)

	context = {
		'spider': spider_id,
		'items': items,
		'pages': pages,
		'page_count': page_count,
		'zap_from_get': zap_from_get,
		'search_form': search_form
	}

	return render_to_response('spider.html', context, context_instance=RequestContext(request))

