#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from dotenv import load_dotenv, find_dotenv
import time
import os
import sys

# Exceptions
from selenium.common.exceptions import WebDriverException

# Load .env Files
load_dotenv(find_dotenv())

class InstaGram:
    """
        Class for Bot
    """
    def __init__(self, username, password):
        # Initiating
        self.username = username
        self.password = password
        
        # Detect Platform
        if "win" in sys.platform:
            driver = "driver.exe"
        elif "linux" in sys.platform:
            driver = "driver"

        bot = 'firefox'

        # Switch Browser
        if bot == "chrome":
            self.bot = webdriver.Chrome(executable_path="./Drivers/chrome"+driver)
        else:
            self.bot = webdriver.Firefox(executable_path="./Drivers/gecko"+driver)
        
        # Set Window Properties
        self.bot.set_window_position(0, 0)
        self.bot.set_window_size(1224, 800)

    def login(self):
        bot = self.bot
        print('Logging you in...')
        bot.get('https://www.instagram.com/accounts/login/')
        time.sleep(3)
        # find search box
        #search = bot.find_element_by_class_name('ytd-searchbox')
        username = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        # clear the input boxes
        username.clear()
        # send keystrokes to input boxes
        username.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        print('Successfully Logged in...')

        # Accept Popup
        try:
            time.sleep(5)
            popup = bot.find_element_by_class_name('HoLwm')
            popup.click()
        except Exception as e:
            print(e)
            pass
    
    def explore(self):
        # For Automatic explore
        bot = self.bot
        bot.get('https://www.instagram.com/explore/')
        time.sleep(5)
        while True:
            bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(5)
    
    def browse(self):
        # For Automatic explore
        bot = self.bot
        print('Visiting Home Page')
        bot.get('https://www.instagram.com/#')
        time.sleep(5)
        while True:
            print('Loading more posts')
            bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            # like = bot.find_element_by_class_name('fr66n')
            # like.click()
            # print('Post Liked...')
            time.sleep(5)

def main():
    username = os.getenv('i_user')
    password = os.getenv('i_pass')
    insta = InstaGram(username, password)
    insta.login()
    #insta.explore()
    insta.browse()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nYou choose to exit!\n')
    except WebDriverException:
        print('You have closed the window...')