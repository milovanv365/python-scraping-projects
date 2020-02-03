# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
from scrapy.loader.processors import MapCompose, TakeFirst


class QuillItem(Item):
    title = Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
        )
    price = Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
        )
    number = Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )


class InvestingItem(Item):
    title = Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )
    content = Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )
