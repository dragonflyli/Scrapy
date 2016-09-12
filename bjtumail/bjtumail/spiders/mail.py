import scrapy

from bjtumail.settings import USERNAME, PASSWORD


class BJTUSpider(scrapy.Spider):
    name = "bjtumail"
    start_urls = [
        "https://mail.bjtu.edu.cn/"
    ]

    headers = {
    "Host": "mail.bjtu.edu.cn",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://mail.bjtu.edu.cn/coremail/",
    "Cookie": "uid=15120207; domain_name=bjtu.edu.cn; locale=en_US; Coremail.sid=BArmnDIIXDlqTDdbYeIINlLZwaEgMNHq; Coremail=4be86e612db9c661e94f3913676fbd80",
    "Connection": "keep-alive"
    }

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            headers = self.headers,
            formdata={"locate": "en_US", "uid": USERNAME, "nodetect": "false", "domain": "bjtu.edu.cn", "password": PASSWORD},
            callback=self.after_login,
            method="POST",
            url="https://mail.bjtu.edu.cn/coremail/index.jsp?cus=1"
        )
        
    def after_login(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
            print response.body
