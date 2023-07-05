from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Chrome(service=Service('C:/Users/user/Downloads/chromedriver_win32/chromedriver.exe'))
driver.get('https://socialblade.com/')
driver.maximize_window()
keywords = [
'利姆 9尼布尼斯'
,'UncleFat 肥大叔'
,'音湖藤淺歌'
,'赤姫紅葉'
,'星見優樂'
,'白蛇梅伊'
,'尤里‧佛瑞斯特'
,'方夏'
,'林梅'
,'天璇'
,'朵朵子'
,'水手緞帶'
,'紫映遊月'
,'椎南月白'
,'舒狐'
,'夢森'
,'魔海ルナ'
,'原瀬空'
,'蘇蘇susu'
,'蒔蘿'
,'貓宮ゆな'
,'菜姬'
,'米良アイル'
,'角蓮'
,'彌里玖·ミリク'
,'EnnSings'
,'花咲くれは'
,'稻荷七櫻'
,'玖月悠梨娜'
,'蕾雅RheaCorey'
,'小闇'
,'米米縭'
,'熊実愛莉'
,'法斯卡'
,'櫻坂くりこ'
,'神氣小儒'
,'黒羊める'
,'夢見ルノ'
,'喵奈ネコドン'
,'寧音柚希'
,'星眷蕾米'
,'魷魷'
,'虹月'
,'神崎アルファ'
,'胡兎柚月'
,'雨恩'
,'鄲森']
for i, keyword in enumerate(keywords, start=1):
    search_box = driver.find_element(By.XPATH, '//*[@id="SearchInput"]')
    search_box.send_keys(keyword)
    search_box.submit()
    time.sleep(2)
    try:
        element = driver.find_element(By.XPATH, '//*[@id="YouTubeUserTopInfoBlock"]/div[7]/span[2]')
        print(f" {element.text}")
    except NoSuchElementException:
        link = driver.find_element(By.PARTIAL_LINK_TEXT, keyword)
        link.click()
        element = driver.find_element(By.XPATH, '//*[@id="YouTubeUserTopInfoBlock"]/div[7]/span[2]')
        print(f" {element.text}")
    time.sleep(2)

input("Press Enter to close the Browser.")
