from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome(service=Service('C:/Users/user/Downloads/chromedriver_win32/chromedriver.exe'))
keywords = ['李聽','Annin Miru Channel','DeluCat迪鹿','璐洛洛 Ruroro','Rumi ch. 懶貓子','Restya瑞斯提亞']
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

    wait = WebDriverWait(driver, 10)
    link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Super Chat')))
    link.click()  # Now "link" should be a web element, not a string.

    input("Press Enter to close the Browser.")
