# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
	class Meta:
		db_table = "article"
		verbose_name = "Статьи"
		verbose_name_plural = "Статьи"
	article_title = models.CharField(max_length = 200,verbose_name="название статьи")
	article_text = models.TextField(verbose_name="Текст статьи")
	article_date = models.DateTimeField(verbose_name="Дата публикации")
	article_likes = models.IntegerField(default=0)

class Comments(models.Model):
	class Meta():
		db_table = 'comments'

	comments_date = models.DateTimeField(auto_now_add=True)
	comments_text = models.TextField(verbose_name="Текст комментария")
	comments_article = models.ForeignKey(Article)
	comments_from = models.ForeignKey(User)
