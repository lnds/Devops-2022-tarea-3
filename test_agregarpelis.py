from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)
driver.get(
  "http://localhost:8080/"
)

## Encontrar Elementos

import time

print('esperaremos 2 segundos')
time.sleep(2)

driver.find_element(By.ID, "add-movie").click()
print('esperaremos 2 segundos')
time.sleep(2)
driver.find_element(By.NAME, "title").click()
print('esperaremos 2 segundos')
time.sleep(2)
driver.find_element(
  By.NAME, "title").send_keys("Star Wars: episodio IV - Una Nueva Esperanza")
print('esperaremos 2 segundos')
time.sleep(2)
driver.find_element(By.NAME, "year").send_keys("1977")
print('esperaremos 2 segundos')
time.sleep(2)
driver.find_element(By.NAME, "director").send_keys("George Lucas")
print('esperaremos 2 segundos')
time.sleep(2)
driver.find_element(By.NAME, "rating").send_keys("5")
print('esperaremos 2 segundos')
time.sleep(2)
driver.find_element(By.NAME, "review").click()
print('esperaremos 2 segundos')
time.sleep(2)
driver.find_element(By.NAME, "review").send_keys("Muy Buena Epoca")
print('esperaremos 2 segundos')
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".btn").click()

print('esperaremos 2 segundos')
time.sleep(2)

driver.find_element(By.ID, "add-movie").click()
print('esperaremos 2 segundos')
time.sleep(2)
driver.find_element(By.NAME, "title").click()
print('esperaremos 2 segundos')
time.sleep(2)
driver.find_element(
  By.NAME, "title").send_keys("Star Wars: episodio V - El imperio contraataca")
print('esperaremos 2 segundos')
time.sleep(2)
driver.find_element(By.NAME, "year").send_keys("1980")
print('esperaremos 2 segundos')
time.sleep(2)
driver.find_element(By.NAME, "director").send_keys("George Lucas")
print('esperaremos 2 segundos')
time.sleep(2)
driver.find_element(By.NAME, "rating").send_keys("5")
print('esperaremos 2 segundos')
time.sleep(2)
driver.find_element(By.NAME, "review").click()
print('esperaremos 2 segundos')
time.sleep(2)
driver.find_element(By.NAME, "review").send_keys("Excelente Epoca")
print('esperaremos 2 segundos')
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".btn").click()

print('esperaremos 2 segundos')
time.sleep(3)

print('esperaremos 2 segundos')
time.sleep(2)

driver.find_element(By.LINK_TEXT, "Dune").click()
print('esperaremos 2 segundos')
time.sleep(2)
driver.find_element(By.NAME, "review").click()
print('esperaremos 2 segundos')
time.sleep(2)
element = driver.find_element(By.NAME, "review")
actions = ActionChains(driver)
driver.find_element(By.NAME, "review").clear()
driver.find_element(
  By.NAME,
  "review").send_keys("Gran Adaptacion de una novela de ciencia ficcion")
print('esperaremos 2 segundos')
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".btn").click()

print('esperaremos 2 segundos')
time.sleep(3)

driver.find_element(By.LINK_TEXT, "Elvis").click()
print('esperaremos 2 segundos')
time.sleep(2)
driver.find_element(By.NAME, "review").click()
print('esperaremos 2 segundos')
time.sleep(2)
element = driver.find_element(By.NAME, "review")
actions = ActionChains(driver)
driver.find_element(By.NAME, "review").clear()
driver.find_element(
  By.NAME, "review").send_keys("Buena película biográfica estilizada del Rey")
print('esperaremos 2 segundos')
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".btn").click()
print('Fin')
