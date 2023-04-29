# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class Douban250Pipeline:

    def open_spider(self, spider):
        self.f = open('./temp.csv', 'a', encoding="utf-8")

    def close_spider(self, spider):
        self.f.close()

    def process_item(self, item, spider):
        self.f.write(str(item["name"]))
        self.f.write(",")
        self.f.write(str(item["url"]))
        self.f.write("\n")
        return item