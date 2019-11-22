#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: Cyber71_2.py
# Created: Sunday, 29th September 2019 6:49:46 pm
# Author: Rakibul Yeasin (ryeasin03@gmail.com)
# -----
# Last Modified: Sunday, 29th September 2019 7:17:07 pm
# Modified By: Rakibul Yeasin (ryeasin03@gmail.com)
# -----
# Copyright (c) 2019 Slishee
###
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

target = "https://docs.google.com/forms/d/1mUvBfUdyHXxVEDcfbfaI8VUfiBfKt4fDzBM3tJLGlhM/viewform"
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

    # Load Target
    bot.get(target)
    time.sleep(3)

    email = bot.find_element_by_name('entry.1045781291')
    name = bot.find_element_by_name('entry.2005620554')
    number = bot.find_element_by_name('entry.1166974658')
    profession = bot.find_element_by_name('entry.1065046570')
    submit = bot.find_element_by_class_name('quantumWizButtonEl')

    email.clear()
    email.send_keys(ran(5) + '@' + mail_domain[random.randint(0, 3)])

    name.clear()
    name.send_keys(ran(4) + ' ' + ran(5))

    number.clear()
    number.send_keys('01' + str(random.randint(1000000, 9999999)))

    profession.clear()
    profession.send_keys(ran(5))

    submit.click()

    time.sleep(random.randint(3, 5))

    bot.quit()


if __name__ == "__main__":
    while True:
        try:
            main()
        except Exception:
            print(Exception)
    # main()
