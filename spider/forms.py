#! coding: utf-8
from django import forms

class SearchForm(forms.Form):

	search = forms.CharField(label='Поиск:', max_length=200)

	# def __init__(self, initial={}, *args, **kwargs):
		# super(SearchForm, self).__init__(*args, **kwargs)
		# self.fields['search'].initial = initial.get('search')

	def clean_search(self):
		search = self.cleaned_data['search']
		search = search.encode('utf-8').lower().strip('*./:,?!+-=&?\'"')

		if len(search) < 1:
			raise forms.ValidationError("Введите в поиск корректную строку (более одного символа)")

		return search
	
