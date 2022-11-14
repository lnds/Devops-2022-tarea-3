from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)
driver.get("127.0.0.1:8080")


## Encontrar Elementos

import time

print('esperaremos 2 segundos' )
time.sleep(2)
driver.find_element(By.ID, "add-movie").click()
print('esperaremos 2 segundos' )
time.sleep(2)
driver.find_element(By.NAME, "title").click()
print('esperaremos 2 segundos' )
time.sleep(2)
driver.find_element(By.NAME, "title").send_keys("Star War")
print('esperaremos 2 segundos' )
time.sleep(2)
driver.find_element(By.NAME, "year").send_keys("1981")
driver.find_element(By.NAME, "director").send_keys("Jeoge Lucas")
driver.find_element(By.NAME, "rating").send_keys("5")
driver.find_element(By.NAME, "review").click()
driver.find_element(By.NAME, "review").send_keys("Muy Buena Epoca")
driver.find_element(By.CSS_SELECTOR, ".btn").click()