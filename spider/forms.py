#! coding: utf-8
from django import forms

class SearchForm(forms.Form):
	search = forms.CharField(label='Поиск:', max_length=200)
