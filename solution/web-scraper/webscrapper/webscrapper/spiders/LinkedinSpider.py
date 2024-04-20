import logging
import scrapy
from selenium import webdriver
from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse
import re
import unicodedata

from colorama import Fore
from cookies import cookies

class LinkedinScrapperSettings:
    login_page_url = "https://www.linkedin.com/login"

    account_email = 'bhlmock1@gmail.com'
    account_password = "0eZyExduckiQ0Zhsgb8Y"

    login_email_id = "username"
    login_password_id = "password"
    login_button_selector = """#organic-div > form > div.login__form_action_container > button"""

    show_all_posts_xpath = """//*[@id="profile-content"]/div/div[2]/div/div/main/section[4]/footer/a/span"""
    name_selector = """/html/body/div[5]/div[4]/div/div/div[2]/div/div/main/section[1]/div[2]/div[2]/div[1]/div[1]/span/a/h1"""
    description_xpath = """//*[@id="profile-content"]/div/div[2]/div/div/main/section[1]/div[2]/div[2]/div[1]/div[2]"""
    organization_xpath = """//*[@id="profile-content"]/div/div[2]/div/div/main/section[1]/div[2]/div[2]/ul/li/button/span/div/text()"""



class LinkedinScraper(scrapy.Spider):
    name = 'LinkedinScraper'

    def __init__(self, linkedin_profile_urls,    
                show_all_posts_selector_or_xpath : [str, bool],
                posts_button_selector_or_xpath : [str, bool],
                reactions_button_selector_or_xpath : [str, bool],
                comments_button_selector_or_xpath : [str, bool],
                post_oldness_max_tolerance : int,
                max_pages : int,
                *args, **kwargs):
        super(LinkedinScraper, self).__init__(*args, **kwargs)
        self.start_urls = [LinkedinScrapperSettings.login_page_url]
        self.profile_urls = [linkedin_profile_urls] if linkedin_profile_urls else []

        # The general idea is, that the user can specify either a selector or an xpath 
        # for each of the items needed to be scraped. This is done by passing a list,
        # where the first element is the string and the second element is a boolean
        # indicating whether the first element is a selector or an xpath.
        # (0 - selector, 1 - xpath)
    
        # Selector or xpath for the button that shows all comments
        self.show_all_posts_selector_or_xpath = show_all_posts_selector_or_xpath
        self.posts_button_selector_or_xpath = posts_button_selector_or_xpath
        self.reactions_button_selector_or_xpath = reactions_button_selector_or_xpath
        self.comments_button_selector_or_xpath = comments_button_selector_or_xpath

        # Maximum number of days since the post was published
        self.post_oldness_max_tolerance = post_oldness_max_tolerance

        # Counter for the number of pages scraped
        self.current_page = 0
        self.max_pages = max_pages

        # Setup the Chrome WebDriver with options
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run headless to avoid opening a new browser window
        chrome_options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36") 
        self.driver = webdriver.Chrome(options=chrome_options)


    def parse(self, response):
        #
        # Logging to LinkedIn
        #
        self.log(f"{Fore.GREEN}Loading the LinkedIn login page{Fore.RESET}", logging.DEBUG)
        self.driver.get(LinkedinScrapperSettings.login_page_url))
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//body')))
        self.log("Getting the Selenium WebDriver response", logging.DEBUG)
        selenium_response_text = self.driver.page_source
        self.log("Creating a Selector from the HTML content", logging.DEBUG)
        sel_response = scrapy.http.HtmlResponse(url=self.driver.current_url, body=selenium_response_text, encoding='utf-8')

        self.log(f"{Fore.GREEN}Attempting to log in{Fore.RESET}", logging.INFO)
        email_elem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, LinkedinScrapperSettings.account_email)))
        email_elem.send_keys(LinkedinScrapperSettings.account_email)
        password_elem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, LinkedinScrapperSettings.account_password)))
        password_elem.send_keys(LinkedinScrapperSettings.account_password)
        self.log(f"Wating for the login button to be clickable", logging.INFO)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, LinkedinScrapperSettings.login_button_selector)))
        password_elem.send_keys(Keys.RETURN)
        self.log(f"Waiting for the page to fully load", logging.INFO)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//body'))) 
        self.log(f"{Fore.GREEN}Successfully logged in{Fore.RESET}", logging.INFO)

        #
        #   Scrape all LinkedIn profiles
        #
        for url in self.profile_urls:
            # Prepare the scraped data
            profile_data = {
                "name_surname": "",
                "organization": "",
                "description": "",
                "posts": []
            }

            self.log(f"Loading the web page", logging.DEBUG)
            self.driver.get(self.profile_urls[0]) 
            self.log("Waiting for the page to fully load", logging.DEBUG)
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//body'))) 
            self.log("Getting the Selenium WebDriver response", logging.DEBUG)
            selenium_response_text = self.driver.page_source
            self.log("Creating a Selector from the HTML content", logging.DEBUG)
            sel_response = scrapy.http.HtmlResponse(url=self.driver.current_url, body=selenium_response_text, encoding='utf-8')

            
            # Get the name, surname, organization and description
            


            #
            # Select the button that shows all comments, click it and wait for the new page to load
            #
#            self.log("Scrolling select all posts button into view", logging.INFO)
#            select_all_posts_button = self.evaluate_selector_or_xpath(sel_response, self.show_all_posts_selector_or_xpath)
#            self.driver.execute_script("arguments[0].scrollIntoView(true);", select_all_posts_button)
#            self.log(f"{Fore.GREEN}Selecting show all comments button{Fore.RESET}", logging.DEBUG)
#
#            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(select_all_posts_button))
#            try:
#                self.log("Clicking the button", logging.INFO)
#                select_all_posts_button.click()
#            except WebDriverException:
#                self.log("Normal click failed, clicking the button with JavaScript", logging.INFO)
#                self.driver.execute_script("arguments[0].click();", select_all_posts_button)
#
#            # Wait for the new page to load
#            self.log(f"Waiting for the new page to load", logging.INFO)
#            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//body'))) 
#
#            self.driver.get(response.url) 
#            # Wait for the page to fully load
#            self.log("Waiting for the page to fully load", logging.INFO)
#            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//body'))) 
#
#            # Get the Selenium WebDriver response
#            self.log("Getting the Selenium WebDriver response", logging.INFO)
#            selenium_response_text = self.driver.page_source
#            return selenium_response_text

    def set_cookies(self, cookies):
        """Set hardcoded cookies into Selenium WebDriver, adjusting sameSite values."""
        for cookie in cookies:
            # Adjusting expiry if present
            if 'expirationDate' in cookie:
                cookie['expiry'] = cookie.pop('expirationDate')

            # Correcting sameSite value
            if 'sameSite' in cookie:
                if cookie['sameSite'] == 'no_restriction' or cookie['sameSite'] == 'unspecified':
                    cookie['sameSite'] = 'None'
                elif cookie['sameSite'] == 'lax':
                    cookie['sameSite'] = 'Lax'
                else:
                    cookie['sameSite'] = 'Strict'
            # Finally, add the cookie
            print(f"Adding cookie: {cookie}")
            self.driver.add_cookie(cookie)


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
