import logging
import scrapy
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import unicodedata

from ws.ws.spiders.Worker import *
from colorama import Fore

class LinkedinScrapperSettings:
    login_page_url = "https://www.linkedin.com/login"

    login_email = 'bolof42773@rartg.com'
    login_password = "Orwell911"

    login_email_id = "username"
    login_password_id = "password"
    login_button_selector = """#organic-div > form > div.login__form_action_container > button"""

    show_all_posts_sox = ["""//*[@id="profile-content"]/div/div[2]/div/div/main/section[4]/footer/a/span""", 1]
    name_sox = ["""/html/body/div[5]/div[4]/div/div/div[2]/div/div/main/section[1]/div[2]/div[2]/div[1]/div[1]/span/a/h1""", 1]
    description_sox = ["""//*[@id="profile-content"]/div/div[2]/div/div/main/section[1]/div[2]/div[2]/div[1]/div[2]""", 1]
    organization_sox = ["""//*[@id="profile-content"]/div/div[2]/div/div/main/section[1]/div[2]/div[2]/ul/li/button/span/div""", 1]

    posts_button_sox = ["""//*[@id="content-collection-pill-0"]""", 1]

    not_found_str = "not found"

    activity_append_url = "recent-activity/all/"



class LinkedinScraper(scrapy.Spider):
    name = 'LinkedinScraper'

    def __init__(self, 
                linkedin_profile_urls : list[str],
                user_emails : list[str],
                workers : list[Worker],
                post_oldness_max_tolerance : int,
                max_pages : int,
                *args, **kwargs):
        super(LinkedinScraper, self).__init__(*args, **kwargs)
        self.start_urls = [LinkedinScrapperSettings.login_page_url]
        self.profile_urls = linkedin_profile_urls
        self.user_emails = user_emails
        self.workers = workers

        # The general idea is, that the user can specify either a selector or an xpath 
        # for each of the items needed to be scraped. This is done by passing a list,
        # where the first element is the string and the second element is a boolean
        # indicating whether the first element is a selector or an xpath.
        # (0 - selector, 1 - xpath)

        # Maximum number of days since the post was published
        self.post_oldness_max_tolerance = post_oldness_max_tolerance
        self.user_email = user_emails

        # Counter for the number of pages scraped
        self.current_page = 0
        self.max_pages = max_pages

        # Setup the Chrome WebDriver with options
        chrome_options = Options()
        #chrome_options.add_argument("--headless")  # Run headless to avoid opening a new browser window
        chrome_options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36") 
        self.driver = webdriver.Chrome(options=chrome_options)


    def parse(self, response):

        #
        # Logging to LinkedIn
        #
        self.log(f"{Fore.GREEN}Loading the LinkedIn login page{Fore.RESET}", logging.DEBUG)
        self.driver.get(LinkedinScrapperSettings.login_page_url)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//body')))
        self.log("Getting the Selenium WebDriver response", logging.DEBUG)
        selenium_response_text = self.driver.page_source
        self.log("Creating a Selector from the HTML content", logging.DEBUG)
        sel_response = scrapy.http.HtmlResponse(url=self.driver.current_url, body=selenium_response_text, encoding='utf-8')

        self.log(f"{Fore.GREEN}Attempting to log in{Fore.RESET}", logging.INFO)
        email_elem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, LinkedinScrapperSettings.login_email_id)))
        email_elem.send_keys(LinkedinScrapperSettings.login_email)
        password_elem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, LinkedinScrapperSettings.login_password_id)))
        password_elem.send_keys(LinkedinScrapperSettings.login_password)
        self.log(f"Wating for the login button to be clickable", logging.INFO)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, LinkedinScrapperSettings.login_button_selector)))
        password_elem.send_keys(Keys.RETURN)
        self.log(f"Waiting for the page to fully load", logging.INFO)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//body'))) 
        self.log(f"{Fore.GREEN}Successfully logged in{Fore.RESET}", logging.INFO)

        #
        #   Scrape all LinkedIn profiles
        #
        # temporary solution to login
        time.sleep(2)

        for (url, email, worker) in zip(self.profile_urls, self.user_emails, self.workers):
            # Prepare the scraped data
            profile_data = {
                "name_surname": LinkedinScrapperSettings.not_found_str,
                "organization": LinkedinScrapperSettings.not_found_str,
                "description": LinkedinScrapperSettings.not_found_str,
                "posts": []
            }

            self.log(f"{Fore.GREEN}Loading the web page for {url}{Fore.RESET}", logging.DEBUG)
            self.driver.get(url) 
            self.log("Waiting for the page to fully load", logging.DEBUG)
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//body'))) 
            self.log("Getting the Selenium WebDriver response", logging.DEBUG)
            selenium_response_text = self.driver.page_source
            self.log("Creating a Selector from the HTML content", logging.DEBUG)
            sel_response = scrapy.http.HtmlResponse(url=self.driver.current_url, body=selenium_response_text, encoding='utf-8')

            # Temporary solution to load all user data
            time.sleep(2)
            # Scrape the name and surname
            # Wait for it to load
            try:
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[contains(@id, "ember")][1]')))
                #xpath to extract the first h1 text 
                first_a_with_ember = sel_response.xpath('//a[contains(@id, "ember")][1]')
                name = first_a_with_ember.xpath('.//h1/text()').get()
                name = name.strip() if name else LinkedinScrapperSettings.not_found_str
                self.log(f"{Fore.GREEN}name: {name}{Fore.RESET}", logging.DEBUG)
                if name:
                    profile_data["name_surname"] = name
            except TimeoutException:
                profile_data["name_surname"] = LinkedinScrapperSettings.not_found_str


            # Scrape the organization
            # Wait for it to load
            try:
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//ul[contains(@class, "pv-text-details__right-panel")]')))
                ul_elements = sel_response.xpath('//ul[contains(@class, "pv-text-details__right-panel")]')
                first_non_empty_element_text = None
                if ul_elements:
                    first_ul = ul_elements[0]
                    first_non_empty_element_text = first_ul.xpath('.//*[normalize-space(text())][1]/text()').get()
                company = first_non_empty_element_text.strip() if first_non_empty_element_text else LinkedinScrapperSettings.not_found_str
                profile_data["organization"] = company
            except TimeoutException:
                profile_data["organization"] = LinkedinScrapperSettings.not_found_str
            
            self.log(f"{Fore.GREEN}company: {company}{Fore.RESET}", logging.DEBUG)

            # Scrape the description
            # Wait for it to load
            try:
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//main[contains(@class, "scaffold-layout__main")]//div[contains(@class, "text-body-medium break-words")]')))
                description = sel_response.xpath('//main[contains(@class, "scaffold-layout__main")]//div[contains(@class, "text-body-medium break-words")]/text()').get()
                description = description.strip() if description else LinkedinScrapperSettings.not_found_str
                if description:
                    profile_data["description"] = description
            except TimeoutException:
                profile_data["description"] = LinkedinScrapperSettings.not_found_str
            
            self.log(f"{Fore.GREEN}description: {description}{Fore.RESET}", logging.DEBUG)

            #
            #   Scrape the posts   
            #

            # Change to the Activity tab
            posts_url = url + LinkedinScrapperSettings.activity_append_url
            self.log(f"{Fore.GREEN}Loading the web page for {posts_url}{Fore.RESET}", logging.DEBUG)
            self.driver.get(posts_url) 
            self.log("Waiting for the page to fully load", logging.DEBUG)
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//body'))) 
            self.log("Getting the Selenium WebDriver response", logging.DEBUG)
            selenium_response_text = self.driver.page_source
            self.log("Creating a Selector from the HTML content", logging.DEBUG)
            sel_response = scrapy.http.HtmlResponse(url=self.driver.current_url, body=selenium_response_text, encoding='utf-8')

            # Wait for the posts to load
            try:
                ul_element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located( (By.CSS_SELECTOR, "ul.display-flex.flex-wrap.list-style-none.justify-center"))
                )
                li_elements = ul_element.find_elements(By.CSS_SELECTOR, "li.profile-creator-shared-feed-update__container")
                # Get the posts
                processed_posts = 0

                for li in li_elements:
                    processed_posts += 1
                    if processed_posts > 5:
                        break
                    ActionChains(self.driver).move_to_element(li).perform()
                    try:
                        wait = WebDriverWait(self.driver, 10)
                        break_words_span = wait.until(
                            EC.visibility_of(li.find_element(By.CSS_SELECTOR, "span.break-words"))
                        )
                        if break_words_span is not None:
                            self.log(f"{Fore.GREEN}Found post text: {break_words_span.text.strip()}{Fore.RESET}", logging.INFO)
                            profile_data["posts"] += [break_words_span.text.strip()]
                    except TimeoutException:
                        self.log(f"{Fore.RED}Coudn't find text in post{Fore.RESET}", logging.INFO)

            except TimeoutException:
                self.log(f"{Fore.RED}No posts found{Fore.RESET}", logging.INFO)

            # Saving to file is obsolete with the worker.context

            worker.context['linkedin'] = profile_data

            # this yield is obsolete
            yield profile_data

    def closed(self, reason):
        # Close the Selenium WebDriver
        self.driver.quit()

    def choose_by_selector_or_xpath(self, selector_or_xpath : [str, bool]):
        # Return the By method based on the method of selection
        if selector_or_xpath is None:
            return None
        if selector_or_xpath[1] == 0:
            return By.CSS_SELECTOR
        elif selector_or_xpath[1] == 1:
            return By.XPATH
    
    def evaluate_selector_or_xpath(self, html_content, selector_or_xpath : [str, bool]):
        # Return selected html element based on the method of selection
        if selector_or_xpath is None:
            return None
        if selector_or_xpath[1] == 0:
            # selector
            return html_content.css(selector_or_xpath[0])
        elif selector_or_xpath[1] == 1:
            # xpath
            return html_content.xpath(selector_or_xpath[0])
        else:
            # neither selector nor xpath
            return None

    # TODO: This should be moved to a separate file
    def remove_special_characters(self, input_string):
        # Normalize and decompose the Unicode characters
        normalized_string = unicodedata.normalize('NFKD', input_string)
        
        # Filter out the characters that are not in the ASCII set
        ascii_string = ''.join([c for c in normalized_string if not unicodedata.combining(c)])
        
        return ascii_string
