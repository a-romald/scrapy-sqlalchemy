# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from database.connection import db
from database.models import AllData



class BooksPipeline(object):

    def process_item(self, item, spider):                 
            # create a new SQL Alchemy object and add to the db session
            record = AllData(title=item['title'].encode('utf-8'),
                             description=item['description'].encode('utf-8'),
                             price=item['price'].encode('utf-8'),
                             image=item['images'][0]['path'].encode('utf-8'),
                             imageurl=item['images'][0]['url'].encode('utf-8'))
            db.add(record)
            db.commit()

            return item
