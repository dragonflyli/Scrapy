import scrapy
from zhihu.settings import USERNAME, PASSWORD


class ZhiHuSpider(scrapy.Spider):
    name = "zhihu"
    start_urls = ["https://www.zhihu.com/#signin"]

    def parse(self, response):
        return scrapy.FormRequest.from_response(response,
            formdata = {"email": USERNAME, "password": PASSWORD},
            callback = self.after_login,
            method = "POST",
            url = "http://www.zhihu.com/login/email")

    def after_login(self, response):
        print response.body
