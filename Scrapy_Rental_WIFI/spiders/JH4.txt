from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from bs4 import BeautifulSoup
import time
import random
import re
import datetime

do_ip_check = True
do_search_around = True
do_confuse_search = True
do_send_keys_slow = True
do_time_sleep = True

f = open('configure.txt', 'r' , encoding = 'UTF-8')
# 隨機搜尋字
confusion_words = f.readline().replace('\ufeff','')
confusion_words = confusion_words.split(',')
del confusion_words[-1]
# print(confusion_words)

# 隨機搜尋-修飾字
global modification_words_of_confusion
modification_words_of_confusion = f.readline()
modification_words_of_confusion = modification_words_of_confusion.split(',')
del modification_words_of_confusion[-1]
# print(modification_words_of_confusion)

# 保護網址
protect_words = f.readline()
protect_words = protect_words.split(',')
del protect_words[-1]
#print(protect_words)

# 關鍵字
keywords = f.readline()
keywords = keywords.split(',')
del keywords[-1]
#print(keywords)

# 關鍵字-修飾字
modification_words_of_keywords = f.readline()
modification_words_of_keywords = modification_words_of_keywords.split(',')
del modification_words_of_keywords[-1]
# print(modification_words_of_keywords)

# 目標網址
target_url = f.readline()
target_url = target_url.split(',')
del target_url[-1]
# print(target_url)

# 瀏覽頁面1-9
surf_page_times = f.readline()
surf_page_times = surf_page_times.split(',')
del surf_page_times[-1]
# print(surf_page_times)

# 頁面停留10-90
page_sleep_times = f.readline()
page_sleep_times = page_sleep_times.split(',')
del page_sleep_times[-1]
# print(page_sleep_times)

# 執行時間
exercise_time = f.readline()
exercise_time = exercise_time.split(',')
del exercise_time[-1]
# print(exercise_time)

spt0 = int(surf_page_times[0])
spt1 = int(surf_page_times[1])

pst0 = int(page_sleep_times[0])
pst1 = int(page_sleep_times[1])

def click_keywords(driver):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "_WGk"))
    )
    elements = driver.find_elements_by_class_name('_WGk')
    target_index = list()
    for ii in range(len(elements)):
        if(not target_url):
            if(not is_protect_word(elements[ii].text)):
                target_index.append(ii)
        else:
            if(is_target_url(elements[ii].text)):
                target_index.append(ii)
            
    target2 = '//h3/a[2]'
    elements2 = driver.find_elements_by_xpath(target2)
    r_num = random.choice(target_index)
    if(do_time_sleep):
        time.sleep(2)
    print(elements[r_num].text)
    elements2[r_num].click()
    return search_around(driver, random.randint(spt0,spt1),"")

def is_exercise_time():
    hour = datetime.datetime.now().hour
    start = int(exercise_time[0])
    end = int(exercise_time[1])
    if(start > end):
        if(hour >= start or hour < end):
            return True
        else:
            return False
    else:
        if(hour >= start and hour < end):
            return True
        else:
            return False
        
def sleep_until_exercise_time():
    start = int(exercise_time[0])
    end = int(exercise_time[1])
    print('預計運行時間: ',start,'-',end)
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    if(hour > start):
        time.sleep(((start-hour+24)*60+-minute)*60)
    else:
        time.sleep(((start-hour)*60+-minute)*60)


def is_protect_word(text):
    for protect_word in protect_words:
        if(re.search(protect_word, text)):
            return True
    return False

def is_target_url(text):
    for url in target_url:
        if(re.search(url, text)):
            return True
    return False

def search_around(driver ,times, string):
    if(not do_search_around):
        times = 0
    ind = 0
    for i in range(times):
        try:
            if(do_time_sleep):
                time.sleep(random.randint(pst0,pst1))            
            elements = driver.find_elements_by_tag_name('a')
            if(len(elements) == 0):
                ind = ind - 1
                driver.back()
            rand_num = random.randint(0,len(elements)-1)
            elements[rand_num].click()
            ind = ind + 1
#             print(i)
        except Exception as e:
            pass
    return ind
    
def confuse_search(driver, times, times2, scrpit):
    if(not do_confuse_search):
        times = 0
    for i in range(times):    
        driver.execute_script(script); 
        driver.get('https://www.google.com.tw')
        time.sleep(3)
        inputElement = driver.find_element_by_id("lst-ib")
        global modification_words_of_confusion
        modification_words = list(modification_words_of_confusion)
        prefix = ''
        if(random.randint(0,1)):
            prefix = random.choice(modification_words)
            modification_words.remove(prefix)
        suffix = ''
        if(random.randint(0,1)):
            suffix = random.choice(modification_words)  
        confusion_word = random.choice(confusion_words)
        confusion_word = prefix + confusion_word + suffix
        send_keys_slow(inputElement, confusion_word)
        inputElement.submit()
        if(do_time_sleep):
            time.sleep(1)
        try:
            print('confuse-start')
            for ii in range(10):
                try:
                    target2 = '//h3/a[1]'
                    elements = driver.find_elements_by_xpath(target2)
                    random.choice(elements).click()
                    search_around(driver ,times2,'')
                    break;
                except:
                    pass
            print('confuse-end')
        except Exception as e:
#             print(e)
            pass
def send_keys_slow(inputElement, string):
    for i in range(len(string)):
        inputElement.send_keys(string[i])
        if(do_send_keys_slow):
            time.sleep(random.randint(30,150)/100)
def get_current_ip():
    res = requests.get('http://ipinfo.io')
    soup = BeautifulSoup(res.text,'lxml')
    ip = soup.select('p')[0]
    res = re.search("([0-9]{1,3}\.){3}[0-9]{1,3}", ip.text)
    return res.group()

def get_random_country_geolocation():
    country_list = {
        '新北市':(121.6739,24.91571),
        '高雄市':(120.666,23.01087),
        '臺中市':(120.9417,24.23321),
        '臺北市':(121.5598,25.09108),
        '桃園縣':(121.2168,24.93759),
        '臺南市':(120.2513,23.1417),
        '彰化縣':(120.4818,23.99297),
        '屏東縣':(120.62,22.54951),
        '雲林縣':(120.3897,23.75585),
        '苗栗縣':(120.9417,24.48927),
        '嘉義縣':(120.574,23.45889),
        '新竹縣':(121.1252,24.70328),
        '南投縣':(120.9876,23.83876),
        '宜蘭縣':(121.7195,24.69295),
        '新竹市':(120.9647,24.80395),
        '基隆市':(121.7081,25.10898),
        '花蓮縣':(121.3542,23.7569),
        '嘉義市':(120.4473,23.47545),
        '臺東縣':(120.9876,22.98461),
#         '金門縣':(118.3186,24.43679),
#         '澎湖縣':(119.6151,23.56548),
#         '連江縣':(119.5397,26.19737),
    }
    country = random.choice(list(country_list.keys()))
    geolocation = country_list[country]
    return country,geolocation[0], geolocation[1]

# cmp_ip = '61.216.99.1'
cmp_ip = '114.41.253.213'
origin_ip = cmp_ip

index2 = 0
while True:
    if(not is_exercise_time()):
        sleep_until_exercise_time()
        
    index2 = index2 +1
    while True:
        try:
            if(not do_ip_check):
                break
            new_ip = get_current_ip()        
#             print(origin_ip)
            if(origin_ip != new_ip and cmp_ip != new_ip):
                origin_ip = new_ip
                print(str(index2)+'------index')
                print(new_ip)
                break
            time.sleep(30)
        except Exception as e:
#             print(e)
            pass
    try:
        country, latitude, longitude= get_random_country_geolocation()
        print(country)
        lf = (random.randint(0,1000)-500)/1000000
        tb = (random.randint(0,1000)-500)/1000000
        script = '''
          window.navigator.geolocation.getCurrentPosition = function(success) {
            var position = { coords : { latitude: "%s", longitude: "%s" } }; 
            success(position);
          }
        ''' % (latitude+lf, longitude+tb)
        driver = webdriver.Chrome()
        driver.delete_all_cookies()
        

        driver.switch_to_window('')
        driver.maximize_window()

        confuse_search(driver, random.randint(0,1), random.randint(spt0,spt1), script)
        confuse_search(driver, random.randint(0,1), random.randint(spt0,spt1), script)

        
        driver.execute_script(script); 
        driver.get('https://www.google.com.tw')
        time.sleep(3)
        inputElement = driver.find_element_by_id("lst-ib")
        modification_words = list(modification_words_of_keywords)
        prefix = ''
        if(random.randint(0,1)):
            prefix = random.choice(modification_words)
            modification_words.remove(prefix)
        suffix = ''
        if(random.randint(0,1)):
            suffix = random.choice(modification_words)        
        
        keyword = random.choice(keywords)
        keyword = prefix + keyword + suffix
        send_keys_slow(inputElement, keyword)
        driver.execute_script(script); 

        inputElement.submit()
        driver.execute_script(script);
#         time.sleep(3)
#         driver.refresh()
#         element = driver.find_element_by_xpath('//*[@id="nav"]/tbody/tr/td[3]/a')
#         element.click()
#         time.sleep(10)
        try:
            ind = click_keywords(driver)
            if(random.randint(0,1)):
                for j in range(ind):
                    try:
                        driver.back()
                        time.sleep(1)
                        elements = driver.find_elements_by_class_name('_WGk')
                        click_keywords(driver)
                        break
                    except Exception as e:
                        pass
        except Exception as e:
            print(e,'--a')
            pass
            
        confuse_search(driver, random.randint(0,1),random.randint(spt0,spt1), script)
        driver.delete_all_cookies()
    except Exception as e:
        print(e,'--b')
        pass
    finally:
        driver.quit()


    

