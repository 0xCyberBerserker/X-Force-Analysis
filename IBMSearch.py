#!/usr/bin/python3
import os
from telnetlib import IP
import os.path
import argparse
import urllib.request as urllib
import urllib.request as urlRequest
import urllib.parse as urlParse
import platform

from PIL import Image
from selenium import webdriver

import time

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from pygments import highlight, lexers, formatters
from dotenv import load_dotenv

parser = argparse.ArgumentParser(
    description='This program utilizes Exchange from IBM to perform queries about IP addresses and Hashes and makes a ScreenShot.'
)
# Inputs
required = parser.add_mutually_exclusive_group()

required.add_argument(
    "-i",
    "--ip",
    help="lookup a single IP address and make a screenshot",
    action="store")

required.add_argument(
    "-l",
    "--list",
    help="lookup for a list of IPs. Usage: python exchangeSearch.py -l List.txt to open various tabs in the web browser with the IPs given on the list."
)

"""
required.add_argument(
    "--hash",
    help="lookup a single hash",
    action="store")
"""
"""
required.add_argument(
    "-l",
    "--list",
    help="lookup a list of IPs",
    action="store")
"""
args = parser.parse_args()



def imgShow(DATA):
    img="X-Force_"+DATA+'.png'
    if(platform.system() == "Windows"):
        os.system('start '+img)
    else:
        os.system("shotwell "+img)



def listScan(DATA):
    list = open(DATA, 'r')
    Lines = list.readlines()
    count = 0
    options = webdriver.ChromeOptions()
    options.headless = True
    if(platform.system() == "Windows"):
        #Windows
        driver = webdriver.Chrome("./chromedrivers/chromedriver.exe")
    else:
        #Linux
        driver = webdriver.Chrome("./chromedrivers/chromedriver")
    
    
    for line in Lines:
        count +=1
        URL = "https://exchange.xforce.ibmcloud.com/ip/"+line
        #options.add_experimental_option("detach", True)
        #Open a New Window
        driver.execute_script("window.open('');")
        # Switch to the new window
        driver.switch_to.window(driver.window_handles[count])
        #Load URL
        driver.get(URL)
    time.sleep(1)
    driver.execute_script("alert('Analisis finalizado :D');")
    while True:
        time.sleep(1)

        
        
        
        
        

def takeScreenshot(DATA):
    URL = "https://exchange.xforce.ibmcloud.com/ip/"+DATA
    options = webdriver.ChromeOptions()
    options.headless = True
    if(platform.system() == "Windows"):
        #Windows
        driver = webdriver.Chrome("./chromedrivers/chromedriver.exe")
    else:
        #Linux
        driver = webdriver.Chrome("./chromedrivers/chromedriver")
    driver.get(URL)
    S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
    driver.set_window_size(S('Width'),S('Height'), driver.window_handles[0]) # May need manual adjustment
    driver.set_window_size(1366,1800, driver.window_handles[0]) # Manual Adjusted, like a phone
    driver.set_window_size(1366,1800) # Manual Adjusted
    time.sleep(2)
    driver.find_element_by_tag_name('body').screenshot('X-Force_'+DATA+'.png')
    driver.quit()

def main():
    if args.ip:
        takeScreenshot(args.ip)
        imgShow(args.ip)
    
    if args.list:
        listScan(args.list)
        
    else:
        exit(
            "Error: one of the following arguments are required: -i/--ip, more work in progress")


if __name__ == '__main__':
    main()