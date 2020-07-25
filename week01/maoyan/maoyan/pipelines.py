# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MaoyanPipeline:
    def process_item(self, item, spider):
        title = item['title']
        film_type = item['film_type']
        film_time = item['film_time']
        output = f'|{title}|\t|{film_type}|\t|{film_time}|\n\n'
        with open('./maoyanmovie2.txt', 'a+', encoding='utf-8') as article:
            article.write(output)
        return item
