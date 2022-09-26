from selenium import webdriver
from selenium.webdriver.common.by import By
from cgitb import text



link = 'https://www.youtube.com'
browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get(link)

search = browser.find_element(By.XPATH, '//input[@id="search"]')
search.send_keys('adele')



search_btn = browser.find_element(By.XPATH, '//button[@id="search-icon-legacy"]')
search_btn.click()


search_res = browser.find_elements(By.CSS_SELECTOR, '#contents.style-scope ytd-item-section-renderer>#contents>.style-scope.ytd-item-section-renderer')

adele_list = []
for i in range(0, 3):
    info_list = {}
    info_list['title'] = search_res[i].find_element(By.CSS_SELECTOR, '#title-wrapper>.title-and-badge.style-scope.ytd-video-renderer').text
    info_list['view'] = search_res[i].find_element(By.CSS_SELECTOR, '#metadata-line>.style-scope.ytd-video-meta-block:nth-child(1)').text

    adele_list.append(info_list)
    
browser.quit()

def get_view_count(adele_list):
    x = []
    for el in adele_list:
        for k,v in el.items():
            if k == 'view':
                v = v.split()
                if ',' in v[0]:
                    v[0] = v[0].replace(',', '.')
                if float(v[0]) > 5 and v[1] == 'млрд' or float(v[0]) > 1 and v[1] == 'млн':
                    x.append(el)
    return x
print(get_view_count(adele_list))




