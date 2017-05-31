# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
import scrapy

from collections import OrderedDict
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem

from KuaikanSpider.items import *

class KuaikanspiderPipeline(object):

    def process_item(self, item, spider):
        return item

class JsonPipeline(object):

    def __init__(self):
        self.file = codecs.open('newimg.json', 'wb', encoding='utf-8')

    def process_item(self, item, spider):
        line = ''
        picindex = 1
        for image_title, image_url, image_path in zip(item['image_titles'], item['image_urls'], item['image_paths']):
            new_item = ImgSingleItem()
            new_item['image_character'] = item['image_character']
            new_item['image_character'] = picindex
            new_item['image_title'] = image_title
            new_item['image_url'] = image_url
            new_item['image_path'] = image_path
            line += json.dumps(OrderedDict(new_item), ensure_ascii=False, sort_keys=False) + '\n'
            picindex = picindex + 1

        self.file.write(line)
        return item

class ImgDownloadPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        if item['image_urls'] is not None:
            for image_url in item['image_urls']:
                yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem('Item contains no images')
        item['image_paths'] = image_paths
        return item
