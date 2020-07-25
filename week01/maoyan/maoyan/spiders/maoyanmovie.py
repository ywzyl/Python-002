import scrapy
from scrapy.http.cookies import CookieJar
from scrapy.selector import Selector
from maoyan.items import MaoyanItem


class MaoyanmovieSpider(scrapy.Spider):
    name = 'maoyanmovie'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/']

    def start_requests(self):
        url = f'https://maoyan.com/films?showType=3'
        header = {'uuid': '24683140CE3811EA844CCDEB469934448670E978CE994E27872A89F903311ED6'}
        yield scrapy.Request(url=url, callback=self.parse, headers=header)

    def parse(self, response):
        print('****************************')
        print(response.text)
        movies = Selector(response=response).xpath('//div[@class="movie-item-hover"]')
        for movie in movies:
            item = MaoyanItem()
            title = movie.xpath('./a/div/div[1]/span[1]/text()')
            item['title'] = title
            print('-----------')
            print(title)
            film_type = movie.xpath('./a/div/div[2]/text()')
            item['film_type'] = film_type
            print('-----------')
            print(film_type)
            film_time = movie.xpath('./a/div/div[4]/text()')
            item['film_time'] = film_time
            print('-----------')
            print(film_time)
            yield item

