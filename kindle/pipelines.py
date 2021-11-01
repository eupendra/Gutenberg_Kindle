# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.pipelines.files import FilesPipeline
import os
from urllib.parse import urlparse
from slugify import slugify

class CustomDownloadPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
        # print(1)
        actual_file_name = os.path.basename(urlparse(response.url).path)
        print(actual_file_name)
        title = item['Title']
        # print(title)
        # print(slugify(title))
        # print(f'{slugify(title)}-{actual_file_name}')
        return f'{slugify(title)}.mobi'
    