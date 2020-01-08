#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: ytube_view_bot.py
# Created: Tuesday, 7th January 2020 9:24:27 pm
# Author: Rakibul Yeasin (ryeasin03@gmail.com)
# -----
# Last Modified: Tuesday, 7th January 2020 11:58:50 pm
# Modified By: Rakibul Yeasin (ryeasin03@gmail.com)
# -----
# Copyright (c) 2020 Slishee
###

import os
import sys
import time
from selenium import webdriver

class Bot:
    def __init__(self):
        self.bot = webdriver.Firefox()

    def open(self, url):
        bot = self.bot
        bot.get(url)
        time.sleep(25)

    def close(self):
        self.bot.close()

def main(url, n):
    bot = Bot()
    for _ in range(n):
        bot.open(url)
        print("[+] View: ", _ + 1)
    bot.close()

if __name__ == "__main__":
    url = str(input("[*] Your URI: "))
    n = int(input("[*] How many views you want: "))
    main(url, n)
