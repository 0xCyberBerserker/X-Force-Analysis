#!/usr/bin/python3
from genericpath import exists
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
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from pygments import highlight, lexers, formatters
from dotenv import load_dotenv
from selenium.webdriver.common.by import By

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
pathScreenshots='./Screenshots'


def imgShow(DATA):
    img=pathScreenshots+"/X-Force_"+DATA+'.png'
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
    options.add_argument("--headless")
    WINDOW_SIZE = "1920,1080"
    options.add_argument("--window-size=%s" % WINDOW_SIZE)
    options.add_experimental_option("detach", True)
    
    if(platform.system() == "Windows"):
        #Windows
        driver = webdriver.Chrome("./chromedrivers/chromedriver.exe")
    else:
        #Linux
        driver = webdriver.Chrome("./chromedrivers/chromedriver")
    
    
    
    for line in Lines:
        
        URL = "https://exchange.xforce.ibmcloud.com/ip/"+line    
        #Open a New Window
        # Switch to the new window
        driver.switch_to.new_window('tab')
        
        #Load URL
        driver.get(URL)
        count +=1
        driver.switch_to.window(driver.window_handles[count])
        
        ## Trying some DOM manipulation
        time.sleep(1)
        
        
        for i in range(2):
            try:
                driver.find_element(By.ID, 'termsCheckbox').click()
                driver.find_element(By.CLASS_NAME, 'guestlogin').click()
                driver.find_element(By.CSS_SELECTOR, '.featurehint__footer>.btn').click()
                #driver.find_element_by_xpath("/html/body/div/div/div[4]/div[2]/p/a").click()
                break
            except NoSuchElementException as e:
                print('Retrying')
                #time.sleep(1)
        #else:
        #    raise e
        
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[0])
    driver.close()
    print('Finished Opening Tabs. It`s time to analyze :D')
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
    time.sleep(1)
    driver.find_element(By.ID, 'termsCheckbox').click()
    driver.find_element(By.CLASS_NAME, 'guestlogin').click()
    driver.find_element(By.CSS_SELECTOR, '.featurehint__footer>.btn').click()
    S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
    driver.set_window_size(S('Width'),S('Height'), driver.window_handles[0]) # May need manual adjustment
    driver.set_window_size(1366,1800, driver.window_handles[0]) # Manual Adjusted, like a phone
    driver.set_window_size(1366,1800) # Manual Adjusted
    time.sleep(2)
    
    
    isExist =os.path.exists(pathScreenshots)
    if not isExist:
        os.makedirs(pathScreenshots)

    driver.find_element(By.TAG_NAME, 'body').screenshot(''+pathScreenshots+'/X-Force_'+DATA+'.png')
    driver.quit()

def main():
    if args.ip:
        takeScreenshot(args.ip)
        imgShow(args.ip)
    
    if args.list:
        listScan(args.list)
        
    else:
        exit(
            "Error: one of the following arguments are required: -i/--ip, -l/--list more work in progress")


if __name__ == '__main__':
    main()