#!/usr/bin/env python3

import os
import sys
import time
import requests as rq
import multiprocessing as mp
from urllib.parse import quote
from bs4 import BeautifulSoup
from selenium import webdriver


# Global Variables
data = mp.Queue()

def loading(title, progress):
    length = 30  # modify this to change the length
    block = int(round(length * progress))
    msg = f'{title}: [{"#"*block} {"-"*(length-block)}] {round(progress*100, 2)}%'
    if progress >= 1:
        msg += " DONE!\n"
    print(msg, end="\r", flush=True)

def search(dork):
    urls = []
    header = {
        "Host": "www.google.com",
        "User-Agent": "Mozilla/5.0 (X11 Linux x86_64 rv: 68.0) Gecko/20100101 Firefox/68.0",
        "Accept": "text/html, application/xhtml+xml, application/xml",
        "Accept-Language": "en-US, en",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Cookie": "CGIC = Ij90ZXh0L2h0bWwsYXBwbGljYXRpb24veGh0bWwreG1sLGFwcGxpY2F0aW9uL3htbDtxPTAuOSwqLyo7cT0wLjg",
        "Upgrade-Insecure-Requests": "1"
    }
    base = "https://www.google.com/search?q="
    target = base + dork
    # response = rq.get(target, headers=header)
    response = rq.get(target)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        try:
            url = soup.findAll('a', href=True)
            for i in url:
                link = i["href"]
                if link.startswith("http"):
                    urls.append(link)
        except Exception as e:
            print(f"[-] Error: {e}")
    # elif response.status_code == 429:
    #     header = {
    #         "Host": "www.bing.com",
    #         "User-Agent": "Mozilla/5.0 (X11 Linux x86_64 rv: 68.0) Gecko/20100101 Firefox/68.0",
    #         "Accept": "text/html, application/xhtml+xml, application/xml",
    #         "Accept-Language": "en-US, en",
    #         "Accept-Encoding": "gzip, deflate, br",
    #         "DNT": "1",
    #         "Connection": "keep-alive",
    #         "Cookie": "MUID=3AF55B504EB26CEB287156C94AB26F9F; MUIDB=3AF55B504EB26CEB287156C94AB26F9F; ASPSESSIONIDACRACQSB=LBJHDNBCFBIBCBDCDIIODIIB; _EDGE_S=mkt=en-bd&SID=2734949C4EE069B103159A804F6B687E; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=3CC69E292F914BBCB131CD3FBFC247B1&dmnchg=1; SRCHUSR=DOB=20191122&T=1574441045000; _SS=SID=2734949C4EE069B103159A804F6B687E&bIm=798&HV=1574441666; SRCHHPGUSR=CW=887&CH=658&DPR=1&UTC=360&WTS=63710037819; ipv6=hit=1574444627631&t=4",
    #         "Upgrade-Insecure-Requests": "1",
    #         "Cache-Control": "max-age = 0",
    #         "TE": "Trailers"
    #     }

    #     base = "https://www.bing.com/search?q="
    #     target = base + quote(dork)
    #     response = rq.get(target)
    #     print(response.text)
    #     soup = BeautifulSoup(response.text, "html.parser")
    #     try:
    #         url = soup.findAll('a', href=True)
    #         for i in url:
    #             link = i["href"]
    #             if link.startswith("http"):
    #                 urls.append(link)
    #     except Exception as e:
    #         print(f"[-] Error: {e}")
    elif response.status_code == 429:
        base = "https://search.yahoo.com/search?p="
        # https://search.yahoo.com/search?p=inurl%3A%2F%3Fop%3Dregistration&b=21 "b"
        target = base + dork
        response = rq.get(target)
        soup = BeautifulSoup(response.text, "html.parser")
        try:
            block = soup.find('div', {'id': 'results'})
            url = block.findAll('a', href=True)
            for i in url:
                urls.append(i["href"])
        except Exception as e:
            print(f"[-] Error: {e}")
    else:
        print("[-] Recaptcha Found!")
    data.put(urls)
    return urls

def savetofile(urls):
    with open("Resources/URLs.txt", "a") as f:
        for url in urls:
            f.write(url + "\n")

def xss(bot, url, payload):
    target = url + payload
    try:
        bot.get(target)
        time.sleep(3)
        alert = bot.switch_to().alert()
        try:
            alert.accept()
        except:
            alert.dismiss()
        return True
    except:
        return False

def main(dork, payload_location):
    # Get URL
    s_process = mp.Process(target=search, args=(dork,))
    s_process.start()

    # Don't Change this block
    pr = 10
    for i in range(pr):
        time.sleep(0.35)
        loading("[+] Getting URLs", i / pr)
    loading("[+] Getting URLs", 1)
    # End Block

    urls = data.get()
    s_process.join()

    # Save the URLS to file
    f_process = mp.Process(target=savetofile, args=(urls,))
    f_process.start()

    # Payloads
    if payload_location.startswith("'"):
        payload_location = payload_location[1:-2]
    with open(payload_location, "r") as f:
        payloads = f.readlines()

    # Browser Automation
    if "win" in sys.platform:
        bot = webdriver.Firefox(executable_path="Drivers/geckodriver.exe")
    else:
        bot = webdriver.Firefox(executable_path="Drivers/geckodriver")
    # Set Window Properties
    bot.set_window_position(0, 0)
    bot.set_window_size(1224, 800)

    found, notfound = 0, 0
    for url in urls:
        for payload in payloads:
            res = xss(bot, url, payload)
            if res is True:
                found += 1
            else:
                notfound += 1
            print(f"\r[+] Found: {found}\t[+] Not Found: {notfound}", end="")
    print()
    bot.quit()

if __name__ == "__main__":
    banner = """
Yb  dP .dP"Y8 .dP"Y8     888888 88 88b 88 8888b.  888888 88""Yb
 YbdP  `Ybo." `Ybo."     88__   88 88Yb88  8I  Yb 88__   88__dP
 dPYb  o.`Y8b o.`Y8b     88""   88 88 Y88  8I  dY 88""   88"Yb
dP  Yb 8bodP' 8bodP'     88     88 88  Y8 8888Y"  888888 88  Yb

    Author: Rakibul Yeasin (@dreygur)

    """
    print(banner)
    dork = input("[*] Your Search Query: ")
    payload = input("[*] Payload File: ")
    print()
    main(dork, payload)
