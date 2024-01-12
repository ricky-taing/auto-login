from selenium import webdriver
#from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import time
import os

class Browser:
    browser, service = None, None
    def __init__(self, driver: str):
        self.service = Service(driver)
        #self.browser = webdriver.Firefox(service=self.service)
        self.browser = webdriver.Chrome(service=self.service)
    
    def open_page(self, url: str):
        self.browser.get(url)

    def close_browser(self):
        self.browser.close()
    
    def add_input(self, by: By, value: str, text: str):
        field = self.browser.find_element(by=by, value=value)
        field.send_keys(text)
        time.sleep(1)

    def click_button(self, by: By, value: str):
        button = self.browser.find_element(by=by, value=value)
        button.click()
        time.sleep(1)
    
    def login_leetcode(self, username: str, password: str):
        self.add_input(by=By.ID, value='id_login', text=username)
        self.add_input(by=By.ID, value='id_password', text=password)
        self.click_button(by=By.CLASS_NAME, value='btn-content__2V4r')
        

if __name__ == '__main__':
    #browser = Browser('.\geckodriver-v0.33.0-win64\geckodriver.exe')
    browser = Browser('.\chromedriver-win64\chromedriver.exe')
    load_dotenv('.\secret.env')
    leet_user = os.getenv('LEETCODE_USER')
    leet_pass = os.getenv('LEETCODE_PASSWORD')

    browser.open_page('https://leetcode.com/accounts/login/')
    time.sleep(3)

    browser.login_leetcode(leet_user, leet_pass)
    time.sleep(30)

    #browser.close_browser()