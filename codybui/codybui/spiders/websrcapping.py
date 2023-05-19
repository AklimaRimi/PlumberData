import scrapy
import time
from scrapy.spiders import SitemapSpider
from datetime import date
import os
import urllib.request
from PIL import Image
import requests
from io import BytesIO
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


class sitemapsScrapping(SitemapSpider):
    name = 'product'
    allowe_domains = ['plumbingsales.com.au']
    sitemap_urls = ['https://plumbingsales.com.au/sitemap.xml']
    
    sitemap_rules = [
        (r'^(.*\/){4,}.*$|^(.*-){5,}.*$', 'start'),
    ]
    
    
    def parse(self, response):        
        time.sleep(5)
        self.driver.get(response.url)
        
        img_links = []
        
        while True:
            try:
                next = self.driver.find_element(By.CLASS_NAME,"fotorama__arr fotorama__arr--next")
                url= response.urljoin(response.css('img[class="product-image-photo default_image"]::attr(src)').get())
                url = url.replace('058489d41f34e884181df59c6b39a71e','d5cb4eb5fe259c9a4975b807d295fa24')
                img_links.append(url)
            except:
                yield scrapy.Request(response.url,self.data_parse, meta={'img_links':img_links})
                break
            
        self.driver.close()
    def data_parse(self,response):
        category = str(response.css('span[itemprop="name"]::text')[1].get())
        cat_list = response.css("ul[class='items']")
        
        category_dict=[]
        link_list = cat_list.css("a[itemprop='item']::attr(href)").getall()
        name_list = cat_list.css("span[itemprop='name'] ::text").getall()
        
        for i in range(len(link_list)):
            category_dict.append({
                'name' : name_list[i],
                'link' : link_list[i],
            })
        
        
        url= response.urljoin(response.css('img[class="product-image-photo default_image"]::attr(src)').get())
        url = url.replace('058489d41f34e884181df59c6b39a71e','d5cb4eb5fe259c9a4975b807d295fa24')
        if not os.path.exists('images'):
            os.mkdir('images')
        path = 'images/'+category.replace(' ','-')
        
        if not os.path.exists(path):
            os.mkdir(path)  
        img_path = path+'/'+url.split('/')[-1]
        
        image_response = requests.get(url)
        image = Image.open(BytesIO(image_response.content))
        image.save(img_path)
        avail = True if 'Add to Cart' in str(response.body) else False
       
        
        yield{            
            'product_link' : str(response.request.url),
            'product_name': str(response.css("span[data-ui-id='page-title-wrapper']::Text").get()),
            'gst_included': 'True',
            'product_price':str(response.css('span[class="price"]::text')[0].get())[1:],
            'product_unit': 'item',
            'price_currency' : str(response.css('span[class="price"]::text')[0].get())[0],
            'category': category_dict,
            'supplier_name' : 'plumbingsales',
            'scraped_date' : date.today(),
            'image_url': response.meta['img_links'],
            'specifications': str(response.css("div[itemprop='description'] ::text").get()),
            'description': str(response.css('div[class="product attribute pk description"] div.value::text').get()),
            'image_paths' : img_path,
            'stock_availability' : avail,           
            
        }