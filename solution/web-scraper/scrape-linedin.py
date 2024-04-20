import logging as log

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from colorama import Fore

from webscrapper.webscrapper.spiders.LinkedinSpider import LinkedinScraper

def crawl_linkedin():
    linkedin_profile_url = "https://www.linkedin.com/in/kacper-u%C5%9Bci%C5%84ski-26578a184/"
    show_all_posts_selector_or_xpath = ["#profile-content > div > div.scaffold-layout.scaffold-layout--breakpoint-xl.scaffold-layout--main-aside.scaffold-layout--reflow.pv-profile.pvs-loader-wrapper__shimmer--animate > div > div > main > section:nth-child(2) > footer > a > span']", 0]

    posts_button_selector_or_xpath = ["button[data-control-name='comments_all_comments_button']", 0]
    reactions_button_selector_or_xpath = ["button[data-control-name='comments_all_comments_button']", 0]
    comments_button_selector_or_xpath = ["button[data-control-name='comments_all_comments_button']", 0]
    post_oldness_max_tolerance = 30

    process = CrawlerProcess(get_project_settings())
    process.crawl(LinkedinScraper,
                linkedin_profile_url,
                show_all_posts_selector_or_xpath,
                posts_button_selector_or_xpath,
                reactions_button_selector_or_xpath,
                comments_button_selector_or_xpath,
                post_oldness_max_tolerance,
                max_pages=1)

    log.info(f"{Fore.GREEN}Starting the crawling process.{Fore.RESET}")
    process.start()  # the script will block here until the crawling is finished
    log.info(f"{Fore.GREEN}Crawling process finished.{Fore.RESET}")

if __name__ == '__main__':
    crawl_linkedin()
