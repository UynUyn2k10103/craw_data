from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep
import random

driver = webdriver.Chrome()

label = 'giao-duc-huong-nghiep'
url = f"https://dantri.com.vn/{label}.htm"
driver.get(url)


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
        all_posts = page_source.find_all('h3', class_ = "news-item__title")
        all_posts.extend( page_source.find_all('h2', class_ = "news-item__title"))
        for post in all_posts:
            post_source = BeautifulSoup(str(post))
            
            link_post = (post.find('a')).get('href')
            link_post = str(link_post)
            if link_post not in all_links:
                all_links.append('https://dantri.com.vn' + link_post)
        if len(all_links) >= 1000: 
            break
        page += 1
        
        print("so post: ", len(all_posts))
        print("So link: ",len(all_links))
        url = f'https://dantri.com.vn/{label}/trang-{page}.htm'
        driver.get(url)
        
        sleep(random.randint(1, 3))
    except:
        continue
    
print(all_links)
import json
filename = 'link_giao_duc_baodantri.json'
with open(filename, 'w+') as f:
    json.dump(all_links, f)
sleep(1)
driver.close()