# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient

from config import COLLECTION_NAME, PASSWORD, USER, HOST, DB_NAME


class DifcScraperPipeline:
    def __init__(self):
        self.cluster = MongoClient(
            f"mongodb+srv://{USER}:{PASSWORD}@{HOST}/{DB_NAME}?retryWrites=true&w=majority")
        db = self.cluster[DB_NAME]
        self.collection = db[COLLECTION_NAME]

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item
