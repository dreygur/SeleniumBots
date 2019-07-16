#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv, find_dotenv
import time
import sys
import os

# Exceptions
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import WebDriverException

# Load .env Files
load_dotenv(find_dotenv())

class TwitterBot:
    """
        Bot Class
        Defines basic functionalities
    """
    def __init__(self, bot, username,  password):
        self.username = username
        self.password = password

        # Detect Platform
        if "win" in sys.platform:
            driver = "driver.exe"
        elif "linux" in sys.platform:
            driver = "driver"

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
        bot.get("https://twitter.com/login/")
        time.sleep(3)
        email = bot.find_element_by_xpath("//*[@id=\"page-container\"]/div/div[1]/form/fieldset/div[1]/input")
        password = bot.find_element_by_xpath("//*[@id=\"page-container\"]/div/div[1]/form/fieldset/div[2]/input")
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    def like(self, keyword):
        bot = self.bot
        bot.get("https://twitter.com/search?q={0}&src=typd".format(keyword))
        time.sleep(3)

        while True:
            bot.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(3)
            tweets = bot.find_elements_by_class_name("tweet")
            links = [i.get_attribute("data-permalink-path") for i in tweets]
            # print(links)
            for link in links:
                bot.get("https://twitter.com" + link)
                try:
                    bot.find_element_by_class_name("HeartAnimation").click()
                    time.sleep(10)
                except Exception as e:
                    print(e)
                    time.sleep(60)

def main(keyword, bot):
    twit = TwitterBot(bot, os.getenv("user"), os.getenv("pass"))
    twit.login()
    twit.like(keyword)

if __name__ == "__main__":
    try:
        keyword = sys.argv[1]
        if len(sys.argv) > 2:
            bot = sys.argv[2]
        main(keyword, 'firefox')
    except IndexError:
        print("You must specify the search term...")
    except NoSuchWindowException:
        print("You Closed the window...")
    except WebDriverException:
        sys.exit()