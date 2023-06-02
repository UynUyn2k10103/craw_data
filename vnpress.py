from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

class Item:
    def __init__(self, label):
        self.title = ''
        self.description = ''
        self.link = ''
        self.label = label
    def function(self, browser):
        self.title = browser.find_element_by_class_name(name='title-detail').text
        self.description = browser.find_element_by_class_name(name = 'description').text
        self.link = browser.current_url

browser = webdriver.Chrome(executable_path = 'chromedriver.exe')


browser.get('https://vnexpress.net')

# listClass = ['thethao','suckhoe', 'kinhte', 'giaoduc', 'giaitri']
sleep(1)
home_link = browser.find_element_by_xpath('/html/body/header/div/a[1]')
home_link.click()
sleep(1)
page = browser.find_element_by_xpath('/html/body/section[2]/section/div/div[2]/div/div[1]/div/div/ul[12]/li[1]/a')
page.click()
sleep(1)

list_item = browser.find_elements_by_id("automation_TV0")

# list_item = browser.find_elements_by_class_name(name = 'title-news')

# list_ans = []
for item in list_item:
    print(item.text)
    # browser.find_element_by_link_text(item.text).click()
    # a = Item('suckhoe')
    # a.function(browser)
    # list_ans.append(a)
    # sleep(1)
    # browser.back()

# print(list_ans)

# button_next = browser.find_element_by_xpath('/html/body/div[3]/div/div/div/a[5]')
# button_next.click()
# sleep(2)

# Quay lai trang truoc
# browser.back()
# sleep(2)
browser.close()

