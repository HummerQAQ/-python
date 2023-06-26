from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service('/usr/local/bin/chromedriver'))
driver.get("http://google.com")

search_box = driver.find_element(By.NAME, 'q')  # Find the search box
search_box.send_keys('Youtube playboard')  # Enter 'youtube playboard' in the search box
search_box.submit()  # Submit the form

# Wait for the page to change (Google's search results have URL starting with 'https://www.google.com/search')
WebDriverWait(driver, 10).until(EC.url_contains('https://www.google.com/search'))

print(driver.current_url)  # Print the current URL

input("Press Enter to close the browser...")
