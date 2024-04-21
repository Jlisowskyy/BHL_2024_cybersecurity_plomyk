# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from colorama import Fore
import logging as log
import json

class ScrapyFilesPipeline:
    def process_item(self, item, spider):
        return item

class WebPipeline:
    def __init__(self):
        self.file = None

    def open_spider(self, spider):
        # Opening spider actions, like opening a file to write
        log.info(f"{Fore.GREEN}Opening spider.{Fore.RESET}")
        # self.file = open('items.json', 'w', encoding='utf-8')

    def close_spider(self, spider):
        # Closing spider actions, like closing a file
        log.info(f"{Fore.GREEN}Closing spider.{Fore.RESET}")
        # if self.file:
        #     self.file.close()

    def process_item(self, item, spider):
        # Process each item and write to a file
        log.info(f"{Fore.GREEN}Processing item: {item}{Fore.RESET}")
        
        filename = f"{hash(item['email'])}.json"

        # Open the file in append mode and write the item
        with open(filename, "a", encoding='utf-8') as file:
            json.dump(ItemAdapter(item).asdict(), file, ensure_ascii=False)
            file.write("\n")  # Add a newline to separate items

        return item