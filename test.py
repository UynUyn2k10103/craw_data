from os import path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep
import random

driver = webdriver.Chrome()

url = 'https://vnexpress.net/'
label = 'kinh-doanh'
driver.get(url = url + label)




# # test
# try:
#     print("post in here....")
#     post = BeautifulSoup(str(all_posts[0]))

#     c_link = post.find_all('a')
#     print(c_link[0].get('href'))
# except:
#     print("Not use")
all_links = []

page = 1
while (True):
    try:
        print("Page: ", page)
        tmp_link = []
        page_source = BeautifulSoup(driver.page_source, 'html.parser')
        all_posts = page_source.find_all('h3', class_ = "title-news")
        all_posts.extend( page_source.find_all('h2', class_ = "title-news"))
        for post in all_posts:
            post_source = BeautifulSoup(str(post))
            link_post = (post.find_all('a'))[0].get('href')
            link_post = str(link_post)
            if link_post not in all_links:
                if link_post.split('.')[-1] == 'html':
                    all_links.append(link_post)
        if len(all_links) >= 1500: 
            break

        button_next = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/a[5]')
        button_next.click()
        page += 1
        print("so post: ", len(all_posts))
        print("So link: ",len(all_links))
        sleep(random.randint(1, 3))
    except:
        continue
print(all_links)
import json
with open("link_kinh-doanh.json", 'w+') as f:
    json.dump(all_links, f)
sleep(1)
driver.close()