# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Product(scrapy.Item):
    name = 'Product'
    product_link = scrapy.Field()
    product_name = scrapy.Field( )
    gst_included = scrapy.Field( )
    product_price = scrapy.Field( )
    product_unit = scrapy.Field( )
    price_currency = scrapy.Field( )
    category = scrapy.Field()
    # product_brand = scrapy.Field(input_processor=MapCompose(),
    # output_processor=TakeFirst()) # if you can find it
    supplier_name = scrapy.Field( )
    scraped_date = scrapy.Field()
    image_url = scrapy.Field(default=[])
    stock_availability = scrapy.Field() # To be added
    description = scrapy.Field( )
    image_paths = scrapy.Field()
    specifications = scrapy.Field()