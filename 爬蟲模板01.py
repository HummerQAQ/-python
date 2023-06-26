from selenium import webdriver
from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome(service=Service('/usr/local/bin/chromedriver'))
driver.get("http://google.com")
input("Press Enter to close the browser...")
