# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
# driver = webdriver.Chrome(service=Service('C:/Users/user/Downloads/chromedriver_win32/chromedriver.exe'))
# keywords = ['李聽','Annin Miru Channel','DeluCat迪鹿','璐洛洛 Ruroro','Rumi ch. 懶貓子','Restya瑞斯提亞','浠Mizuki Channel','魔哩煞','森森鈴蘭 / Lily Linglan【箱箱The Box所屬】',' 厄倫蒂兒','稻乙緹','汐Seki Channel','塔芭絲可','烟花蹦蹦蹦 ch. YanHua']
# driver.get("https://playboard.co/en/")
# driver.maximize_window()
# time.sleep(2)
# link = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/header/div[5]/div[2]/a')
# link.click()
# time.sleep(2)
# search_box = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/main/div[2]/form/input[1]') #輸入帳號
# search_box.send_keys('hu110048138@gapp.nthu.edu.tw')
# time.sleep(2)
# search_box = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/main/div[2]/form/input[2]') #輸入帳號
# search_box.send_keys('humm0211')
# link = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/main/div[2]/form/button') #輸入帳號
# link.click()
# time.sleep(5)
#
# for i, keyword in enumerate(keywords, start=1):
#     search_box = driver.find_element(By.NAME, 'q')
#     search_box.send_keys(keyword)
#     search_box.submit()
#     time.sleep(2)
#     # Wait until the search results are loaded
#     WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div/main/div/div/div/div[1]/div[2]/h2/a')))
#     # Click the first search result
#     link = driver.find_element(By.PARTIAL_LINK_TEXT, keyword)
#     link.click()
#     time.sleep(2)
#     element =  driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/main/article/div/div/div/div/div/section[2]/div[2]/div[1]/div[1]')
#     print(f" {element.text}")
#
# input("Press Enter to close the Browser.")

#     #點supderchat
#     link = driver.find_element(By.PARTIAL_LINK_TEXT,'Super Chat').text
#     link.click()
#
#     # Wait until the new page is loaded
#     WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div/main/article/header/div/div/div[3]/div[1]/ul/li[2]')))
#     element1 = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/main/article/div/div/div[2]/div/section[3]/div/table/tbody/tr[3]/td[2]/span') #五月收益
#     element2 = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/main/article/div/div/div[2]/div/section[3]/div/table/tbody/tr[4]/td[2]/span')
#     element3 = element2-element1
#     print(f" {element3.text}")
#
# input("Press Enter to close the Browser.")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(service=Service('C:/Users/user/Downloads/chromedriver_win32/chromedriver.exe'))
keywords = ['李聽','Annin Miru Channel','DeluCat迪鹿','璐洛洛 Ruroro','Rumi ch. 懶貓子','Restya瑞斯提亞','浠Mizuki Channel','魔哩煞','森森鈴蘭 / Lily Linglan【箱箱The Box所屬】',' 厄倫蒂兒','稻乙緹','汐Seki Channel','塔芭絲可','烟花蹦蹦蹦 ch. YanHua']
driver.get("https://playboard.co/en/")
driver.maximize_window()
time.sleep(2)
link = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/header/div[5]/div[2]/a')
link.click()
time.sleep(2)
search_box = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/main/div[2]/form/input[1]') #輸入帳號
search_box.send_keys('hu110048138@gapp.nthu.edu.tw')
time.sleep(2)
search_box = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/main/div[2]/form/input[2]') #輸入帳號
search_box.send_keys('humm0211')
link = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/main/div[2]/form/button') #輸入帳號
link.click()
time.sleep(5)

for i, keyword in enumerate(keywords, start=1):
    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys(keyword)
    search_box.submit()
    time.sleep(2)
    # Wait until the search results are loaded
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div/main/div/div/div/div[1]/div[2]/h2/a')))
    # Click the first search result
    link = driver.find_element(By.PARTIAL_LINK_TEXT, keyword)
    link.click()
    time.sleep(2)
    element =  driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/main/article/header/div/div/div[3]/div[1]/ul/li[2]')
    print(f" {element.text}")

input("Press Enter to close the Browser.")

