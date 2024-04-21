import logging as log

from scrapy.crawler import CrawlerProcess
from scrapy import signals

from scrapy.utils.project import get_project_settings

from colorama import Fore

from ws.ws.spiders.LinkedinSpider import LinkedinScraper
from ws.ws.settings import ITEM_PIPELINES

from ..ConnectionSolution.MainFlowLib import Worker

from time import sleep

def crawl_linkedin(emails : list, urls : list, workers : list[Worker]):
    post_oldness_max_tolerance = 30

    process = CrawlerProcess(get_project_settings())

    process.crawl(LinkedinScraper,
                linkedin_profile_urls = urls,
                user_emails = emails,
                workers = workers,
                post_oldness_max_tolerance = post_oldness_max_tolerance,
                max_pages=1)

    log.info(f"{Fore.GREEN}Starting the crawling process.{Fore.RESET}")
    process.start()  # the script will block here until the crawling is finished
    log.info(f"{Fore.GREEN}Crawling process finished.{Fore.RESET}")

if __name__ == '__main__':
    emails = ['placeholderemail1@email.com', 'placeholderemail2@email.com']
    urls = ['https://www.linkedin.com/in/marcinwaryszak/', 'https://www.linkedin.com/in/mariuszgil/']
    crawl_linkedin(emails, urls)
