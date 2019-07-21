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

class FBBot:
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
            self.bot = webdriver.Firefox(executable_path="./Drivers/gecko"+driver)
        else:
            self.bot = webdriver.Chrome(executable_path="./Drivers/chrome"+driver)
        
        # Set Window Properties
        self.bot.set_window_position(0, 0)
        self.bot.set_window_size(1224, 800)

    def login(self):
        bot = self.bot
        bot.get("https://www.facebook.com/")
        time.sleep(3)
        email = bot.find_element_by_xpath("//*[@id=\"email\"]")
        password = bot.find_element_by_xpath("//*[@id=\"pass\"]")
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

    def privacy(self):
        bot = self.bot
        bot.get("https://www.facebook.com/profile.php")
        time.sleep(5)

        while True:
            public_posts = bot.find_elements_by_class_name('_42ft _4jy0 _55pi _5vto _55_p _2agf _4o_4 _401v _p _1zg8 _3m8n _4jy3 _517h _51sy _59pe')
            for post in public_posts:
                post.click()

def main(keyword, bot):
    fb = FBBot(bot, os.getenv("f_user"), os.getenv("f_pass"))
    fb.login()
    fb.privacy()
    # fb.like(keyword)

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
    except KeyboardInterrupt:
        print('\nYou choose to exit!\n')
    except WebDriverException:
        print('You have closed the window...')