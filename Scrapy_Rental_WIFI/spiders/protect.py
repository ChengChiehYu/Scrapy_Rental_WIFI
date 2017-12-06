import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
 
# available since 2.4.0
from selenium.webdriver.support.ui import WebDriverWait
 
# available since 2.26.0
from selenium.webdriver.support import expected_conditions as EC
import random
 
# 建立 driver
driver = webdriver.Chrome()

# options = webdriver.ChromeOptions()
# prefs = {"profile.default_content_setting_values.geolocation" :2}
# options.add_experimental_option("prefs",prefs)
# driver = webdriver.Chrome(chrome_options=options)
# driver.maximize_window()
times = 1
for i in range(times):
    driver.get("https://www.google.com")
    inputElement = driver.find_element_by_id('lst-ib')
    inputElement.send_keys('徵信')
    inputElement.submit()
    target_words = ('www.twgoodspy',)
#     try:
#         target = '//cite[text()[contains(.,"%s")]]' % random.choice(target_words)
# #         print(target)
#         element = driver.find_element_by_xpath(target)
#         print(element.text)
#         target2 = target+' /../../div[1]/h3/a[2]'
#         print(target2,'---t2')
#         element2 = driver.find_element_by_xpath(target2)
#         element2.click()
#     except Exception as e:
#         print(e)
#         time.sleep(10)
#         driver.quit()
    try:
        target = '//cite[text()[contains(.,"徵信")]]'
#         elements = driver.find_elements_by_xpath(target)
        target2 = target+' /../../div[1]/h3/a[2]'
        print(target2,'---t2')
        elements = driver.find_elements_by_xpath(target2)
        elements[1].click()
#         elements.click()
#         element = element.tag_name
#         for element in elements:
#             print(element.text)
    except Exception as e:
        print(e)
    
    time.sleep(5)
    driver.quit()