# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ImgItem(scrapy.Item):

    image_character = scrapy.Field()
    image_titles = scrapy.Field()
    image_urls = scrapy.Field()
    image_paths = scrapy.Field()

class ImgSingleItem(scrapy.Item):

    image_character = scrapy.Field()
    image_picindex = scrapy.Field()
    image_title = scrapy.Field()
    image_url = scrapy.Field()
    image_path = scrapy.Field()
