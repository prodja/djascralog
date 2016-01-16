# -*- coding: utf-8 -*-
from django.contrib import admin
from article.models import Article, Comments
from django.apps import apps

# Register your models here.
class ArticleInline(admin.StackedInline):
	model=Comments
	extra=2

class ArticleAdmin(admin.ModelAdmin):
	fields = ['article_title','article_text','article_date']
	inlines = [ArticleInline]
	list_filter = ['article_date']
	list_display = ['article_title']

admin.site.register(Article, ArticleAdmin)