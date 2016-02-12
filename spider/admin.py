from django.contrib import admin
from spider.models import Price_gb

class PriceAdmin(admin.ModelAdmin):
	fields = ['price','code','date']
	list_filter = ['date']
	list_display = ['code']

admin.site.register(Price_gb, PriceAdmin)