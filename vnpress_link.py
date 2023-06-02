from os import write
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep
import random
import csv
import os


def Output(filename, url, label):
    driver = webdriver.Chrome()
    
    with open(filename, mode = 'a', newline = '', encoding = 'utf-8-sig') as f:
        headers = ['Title', 'Description', 'Copus', 'Link', 'Label']
        writer = csv.DictWriter(f, fieldnames = headers)
        if os.path.exists(filename) == False:
            writer.writeheader()
        driver.get(url)

        page_source = BeautifulSoup(driver.page_source, 'html.parser')
        title = driver.find_element_by_class_name('title-detail').text
        description = driver.find_element_by_class_name('description').text
        data_copus = (page_source.find(class_ = 'fck_detail')).find_all('p',class_ = "Normal")

        copus = ''
        for copus_tmp in data_copus:
            copus += " " + copus_tmp.text
        
        writer.writerow({headers[0] : title, headers[1] : description, headers[2] : copus, headers[3]: url, headers[4] : label})
        sleep(random.randint(1, 3))
    driver.close()