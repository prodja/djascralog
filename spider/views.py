#! coding: utf-8
from django.template import RequestContext
from django.shortcuts import render_to_response
from forms import SearchForm
from fns import sel_from_elast
from django.http import HttpResponse


def spider(request, page=1, zap_from_get=''):
	""" кол-во выводимых товаров на одной странице (size)"""
	hits_count=7
	spider_id=1
	curpage = 0
	items = None
	pages=[]
	page_count=0
	__fields = ['name', 'code', 'url','price_reg','price_discount']
	template='spider.html'
	search_form = SearchForm()	

	""" Если запрос пришел с url'а (с постраничника) """ 		
	if request.method == "GET" and request.is_ajax():
	
		""" Если с постраничника пришел текст запроса с формы """
		if zap_from_get:			
			template='items.html'
			""" Делаем запрос в эластик и получаем товары """
			items, pages, page_count = sel_from_elast(zap_from_get, __fields, size_s=hits_count, form_s=int(page)-1)

	elif request.method == "POST" and request.is_ajax():
		""" Если с формы """
		zap_from_get=request.POST.get('search_ajax')
		template='items.html'
		items, pages, page_count = sel_from_elast(zap_from_get, __fields, size_s=hits_count, form_s=int(page)-1)

	context = {
		'spider': spider_id,
		'items': items,
		'pages': pages,
		'page_count': page_count,
		'zap_from_get': zap_from_get,
		'search_form': search_form
	}

	return render_to_response(template, context, context_instance=RequestContext(request))

