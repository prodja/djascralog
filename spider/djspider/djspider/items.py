#! coding: utf-8

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field
from scrapy.item import Item

class GearBestItem(Item):
    url = Field()
    name = Field()
    code = Field()
    price_reg = Field()
    price_discount = Field()
    img = Field()

