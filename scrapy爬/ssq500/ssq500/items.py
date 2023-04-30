# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Ssq500Item(scrapy.Item):
    # define the fields for your item here like:
    center = scrapy.Field()
    chartball01 = scrapy.Field()
    chartball02 = scrapy.Field()
