# -*- coding:UTF-8 -*-

import re

from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from scrapy.http import Request

from KuaikanSpider.items import *

class KuaikanSpider(CrawlSpider):

    name = 'kuaikan'
    start_urls = [
        'http://www.kuaikanmanhua.com/web/comic/26072/'
    ]

    def __init__(self):
        self.website = 'http://www.kuaikanmanhua.com/'
        self.character = 0

    def start_requests(self):

        return [Request(
            self.start_urls[0],
            callback=self.get_img
        )]

    def get_img(self, response):

        self.character = self.character + 1
        l = ItemLoader(item=ImgItem(), response=response)
        l.add_value('image_character', str(self.character))
        l.add_xpath('image_titles', '//*[@id="main"]/div[1]/div[1]/h2/i/text()[2]')
        l.add_xpath('image_urls', '//*[@id="main"]/div[1]/div[3]/img/@src')
        yield l.load_item()

        next_page_url = Selector(response).xpath('//*[@id="main"]/div[1]/div[2]/div/ul/li[3]/a/@href').extract_first()
        if next_page_url is not None:
            yield Request(
                self.website + next_page_url,
                callback=self.get_img
            )
