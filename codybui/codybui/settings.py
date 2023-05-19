
from shutil import which

SELENIUM_DRIVER_NAME = 'chrome'
SELENIUM_DRIVER_EXECUTABLE_PATH ='C:/Users/User/Downloads/chromedriver_win32 (1)'
SELENIUM_DRIVER_ARGUMENTS = ['--headless']


DOWNLOADER_MIDDLEWARES={
    'scrapy_selenium.SeleniumMiddleware': 800
}

BOT_NAME = "codybui"

SPIDER_MODULES = ["codybui.spiders"]
NEWSPIDER_MODULE = "codybui.spiders"

ROBOTSTXT_OBEY = True
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
