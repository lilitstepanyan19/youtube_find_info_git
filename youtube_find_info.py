from selenium import webdriver
from selenium.webdriver.common.by import By
from cgitb import text
import time
import json

link = 'https://www.youtube.com'
browser = webdriver.Chrome()
browser.get(link)

search = browser.find_element(By.XPATH, '//input[@id="search"]')
search.send_keys('adele')

time.sleep(2)

search_btn = browser.find_element(By.XPATH, '//button[@id="search-icon-legacy"]')
search_btn.click()

time.sleep(20)

search_res = browser.find_elements(By.CSS_SELECTOR, '#contents.style-scope ytd-item-section-renderer>#contents>.style-scope.ytd-item-section-renderer')

adele_list = []
for i in range(0, 5):
    info_list = {}
    info_list['title'] = search_res[i].find_element(By.CSS_SELECTOR, '#title-wrapper>.title-and-badge.style-scope.ytd-video-renderer').text
    info_list['view'] = search_res[i].find_element(By.CSS_SELECTOR, '#metadata-line>.style-scope.ytd-video-meta-block:nth-child(1)').text
    info_list['year'] = search_res[i].find_element(By.CSS_SELECTOR, '#metadata-line>.style-scope.ytd-video-meta-block:nth-child(2)').text
    adele_list.append(info_list)

browser.quit()    

adele = json.dumps(adele_list)

adele_file = open("adele.json", "w")
adele_file.write(adele)
adele_file.close()   
    










