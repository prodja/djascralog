#! coding: utf-8

import scrapy
import httplib2
from scrapy import Request
from djspider.items import GearBestItem

class ScrapyTestSpider(scrapy.Spider):
    name = "gearbest"
    allowed_domains = ["www.gearbest.com"]
    start_urls = ["http://www.gearbest.com/car-electronics-c_11247/",
    ]

    def parse(self, response):

        for href in response.xpath("//a[@class='proImg_a']/@href"):
            url = response.urljoin(href.extract())
            yield Request(url, callback=self.parse_product)

        url = response.urljoin(response.xpath("//a[@class='next']/@href")[0].extract())
        yield Request(url, callback=self.parse)

    def parse_product(self, response):
        item=GearBestItem()
        item['url']=str(response.url)
        item['name']=response.xpath('//*[@id="mainWrap"]/div[2]/div/h1/text()').extract()[0]
        item['code']=response.xpath('//*[@id="mainWrap"]/div[2]/div/span[2]/text()').extract()[0]
        preg=response.xpath('//*[@id="market_price"]/text()').extract()
        pdis=response.xpath('//*[@id="unit_price"]/text()').extract()

        item['price_reg']=[]
        item['price_discount']=[]

        if(len(preg)>0):
            item['price_reg'].append(str(preg[0]))
            item['price_discount'].append(str(pdis[0]))
        else:
            item['price_reg'].append(str(pdis[0]))

        img_url=response.xpath('//*[@id="js_jqzoom"]/img/@src').extract()[0]
        item['img']=img_url
        
        return item
