# -*- coding: utf-8 -*-
import scrapy
from catalogue.items import BookItem


class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        # follow links to author pages
        for href in response.css('article.product_pod h3 a::attr(href)'):
            yield response.follow(href, self.parse_book)

        # follow pagination links
        for href in response.css('ul.pager li.next a::attr(href)'):
            yield response.follow(href, self.parse)



    def parse_book(self, response):
    	item = BookItem()

        def extract_with_css(query):
            return response.css(query).extract_first().strip()

        item['title'] = extract_with_css('article.product_page div.product_main h1::text')
        item['description'] = extract_with_css('article.product_page div#product_description + p::text')
        item['price'] = extract_with_css('article.product_page div.product_main p.price_color::text')
        src = response.css('article.product_page div.item.active img::attr(src)').extract_first()
        cover = response.urljoin(src)
        item['image_urls'] = [cover]
        return item



#scrapy crawl books -o books.json -s CLOSESPIDER_PAGECOUNT=5
