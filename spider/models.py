#! coding: utf-8 
from __future__ import unicode_literals
from django.db import models


class Price_gb(models.Model):
	class Meta:
		db_table = "price_gb"
		verbose_name = "Цены gb"

	price = models.FloatField(default=0, verbose_name="Цена товара")
	price_disc = models.FloatField(default=0, verbose_name="Цена со скидкой")
	code=models.TextField(verbose_name="Код товара")
	date = models.DateTimeField(auto_now_add=True)
