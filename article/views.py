from django.shortcuts import render
from django.http.response import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response, redirect
from article.models import Article, Comments
from django.core.exceptions import ObjectDoesNotExist
from forms import CommentForm
from django.core.context_processors import csrf
from django.core.paginator import Paginator
from django.contrib import auth
from django.apps import apps


def articles(request, page_number=1):
	all_articles = Article.objects.all()
	current_page = Paginator(all_articles, 2)
	id_user=auth.get_user(request).id
	return render_to_response('articles.html', {'id_user':id_user, 'curpage':page_number,'articles':current_page.page(page_number), 'username': auth.get_user(request).username})


def article(request, article_id=1):
	comment_form = CommentForm
	args={}
	args.update(csrf(request))
	args['article'] = Article.objects.get(id=article_id)
	args['comments'] = Comments.objects.filter(comments_article_id=article_id)
	args['form'] = comment_form
	args['username'] = auth.get_user(request).username
	return render_to_response('article.html',args)

def addlike(request, article_id, page_id):
    try:
   		if article_id in request.COOKIES:
   			redirect('/articles/page/%s/' % page_id)
   		else:
	   		article = Article.objects.get(id=article_id)
	   		article.article_likes+=1
	   		article.save()
	   		response = redirect('/articles/page/%s/' % page_id)
	   		response.set_cookie(article_id,"test")
   			return response
    except ObjectDoesNotExist:
   		raise Http404
    return redirect('/articles/page/%s/' % page_id)

def addcomment (request, article_id):
	if request.POST and ('pause' not in request.session):
		form = CommentForm(request.POST)
		if form.is_valid():
			id_cur_user=auth.get_user(request).id
			comment = form.save(commit=False)
			comment.comments_article = Article.objects.get(id=article_id)
			comment.comments_from = apps.get_model("auth", "User").objects.all().filter(id=id_cur_user)[0]
			form.save()
			request.session.set_expiry(60)
			request.session['pause']=True
	return redirect('/articles/get/%s/' % article_id)