#!/usr/bin/env python3

from selenium import webdriver
import random
import string
import time
import sys
import os

"""
Fake Dengue Survey Spam In bangladesh
I am gonna spam the spammer :D
"""

# Exceptions
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import WebDriverException

target = "https://docs.google.com/forms/d/e/1FAIpQLSfEqbdTpvh4x_92zUswOOLqvW6tIk7kmOWQIkYjRKsNbNw1tw/viewform"
mail_domain = ['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com']

def ran(length=10):
    """ Random String """
    letters = string.ascii_lowercase + string.ascii_uppercase
    return ''.join(random.choice(letters) for i in range(length))

def main():
    """ Hello """

    # Detect Platform
    if "win" in sys.platform:
        driver = "driver.exe"
    elif "linux" in sys.platform:
        driver = "driver"

    # Webdriver Location
    bot = webdriver.Firefox(executable_path="./Drivers/gecko"+driver)

    # Set Window Properties
    bot.set_window_position(0, 0)
    bot.set_window_size(1224, 800)

    while True:
        # Load Target
        bot.get(target)
        time.sleep(3)

        email = bot.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[1]/div[2]/div/div[1]/div/div[1]/input')
        name = bot.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/input')
        checkboxes = f'//*[@id="mG61Hd"]/div/div[2]/div[2]/div[3]/div/div[2]/div/span/div/div[{random.randint(1, 2)}]/label'
        ages = f'//*[@id="mG61Hd"]/div/div[2]/div[2]/div[4]/div/div[2]/div/span/div/div[{random.randint(1, 6)}]/label'
        number = bot.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[5]/div/div[2]/div/div[1]/div/div[1]/input')
        comments = f'//*[@id="mG61Hd"]/div/div[2]/div[2]/div[6]/div/div[2]/div/span/div/div[{random.randint(1, 4)}]/label'
        submit = bot.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[3]/div[1]/div/div')

        email.clear()
        email.send_keys(ran(5) + '@' + mail_domain[random.randint(0, 3)])

        name.clear()
        name.send_keys(ran(4) + ' ' + ran(5))

        checkbox = bot.find_element_by_xpath(checkboxes)
        checkbox.click()

        age = bot.find_element_by_xpath(ages)
        age.click()

        number.clear()
        number.send_keys('01' + str(random.randint(1000000, 9999999)))

        comment = bot.find_element_by_xpath(comments)
        comment.click()

        submit.click()

        time.sleep(random.randint(5, 10))

if __name__ == "__main__":
    try:
        main()
    except Exception:
        print(Exception)
    