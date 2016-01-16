# -*- coding: utf-8 -*-
from article.models import Comments
from django.forms import ModelForm

class CommentForm(ModelForm):
	class Meta:
		model = Comments
		fields = ['comments_text']
