from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.google.com')
# driver.get('https://summerofcode.withgoogle.com/')

# elem = driver.find_element_by_css_selector('#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input')
# elem = driver.find_element_by_id('lst-ib')
# elem = driver.find_elements(
#     By.XPATH, '//*[@id="tsf"]')
elem=driver.find_element_by_link_text('About')
time.sleep(5)
elem.click()
time.sleep(5)
elem=driver.find_element_by_link_text('Products')
elem.click()
driver.refresh()
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
print(driver.current_url)
# elem.clear()
# elem.send_keys('Python')
# elem.send_keys(Keys.RETURN)
