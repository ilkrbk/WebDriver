import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.tiktok.com/")

searchText = "jordi.koalitic"
time.sleep(3)
browser.find_element_by_css_selector('[name="q"]').send_keys(searchText)
time.sleep(3)
browser.find_element_by_css_selector('[name="q"]').send_keys(Keys.RETURN)
time.sleep(3)
browser.find_element_by_css_selector('[href="/@jordi.koalitic?lang=en"]').send_keys(Keys.RETURN)
time.sleep(3)
resultTitleText = browser.find_element_by_class_name('share-title').text
assert resultTitleText == searchText

time.sleep(10)
browser.quit()