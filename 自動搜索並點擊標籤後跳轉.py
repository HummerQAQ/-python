from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service('/usr/local/bin/chromedriver') #
driver.get("https://playboard.co/en/"） #導向目標網站
search_box = driver.find_element(By.NAME, 'q')  # 導向頁面搜尋欄位
search_box.send_keys('李聽')  # 輸入搜尋內容
search_box.submit() # 提交搜尋內容

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"wrapper"))) #為防止超時問題，等待某個項目出現時，再繼續進行之後動作，最多等待十秒
link = driver.find_element(By.LINK_TEXT,'李聽') #找到頁面上的某個超連結標籤
link.click() #點擊連結標籤並導向至下個頁面

input("Press Enter to close the browser...") #關閉網站頁面
