import logging as log

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from colorama import Fore

from webscrapper.webscrapper.spiders.LinkedinSpider import LinkedinScraper

def crawl_linkedin():
    linkedin_profile_url = "https://www.linkedin.com/in/emilyroseallen/"
    post_oldness_max_tolerance = 30

    process = CrawlerProcess(get_project_settings())
    process.crawl(LinkedinScraper,
                linkedin_profile_url,
                post_oldness_max_tolerance,
                max_pages=1)

    log.info(f"{Fore.GREEN}Starting the crawling process.{Fore.RESET}")
    process.start()  # the script will block here until the crawling is finished
    log.info(f"{Fore.GREEN}Crawling process finished.{Fore.RESET}")

if __name__ == '__main__':
    crawl_linkedin()
