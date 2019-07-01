# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
from scrapy.pipelines.images import ImagesPipeline
from love import settings


class LovePipeline(object):
    def process_item(self, item, spider):
        return item

# 重写scrapy提供的ImagesPipeline
class BMWImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        #这个方法是在发送下载请求前调用
        #这个方法本身就是去发送下载请求的
        request_objs = super(BMWImagesPipeline, self).get_media_requests(item,info) # 获取父类中申请下载的方法
        for request_obj in request_objs:
            request_obj.item = item # 将engine传进来的item赋值给下载器，包含名字和图片地址
        return request_objs

    #重写file_path，用它调用父类的file_path
    def file_path(self, request, response=None, info=None):
        # path = super(BMWImagesPipeline, self).file_path(request,response,info)
        # 没有调用父类的方法，直接调用os.path.basename可以获取到下载地址的文件名！！！
        path = os.path.basename(request.url)
        name = request.item.get('name')
        images_store = settings.IMAGES_STORE
        name_path = os.path.join(images_store,name)
        if not os.path.exists(name_path):
            os.mkdir(name_path)
        image_name = path.replace("full/","")
        image_path = os.path.join(name_path,image_name)
        return image_path