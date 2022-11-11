from selenium import webdriver

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

 

chrome_options = Options()

chrome_options.add_argument('--no-sandbox')

chrome_options.add_argument('--disable-dev-shm-usage')

 

driver = webdriver.Chrome(options=chrome_options)

driver.get("http://localhost:8080/")

driver.set_window_size(1928, 1048)

driver.find_element(By.ID, "add-movie").click()

driver.find_element(By.NAME, "title").click()

driver.find_element(By.NAME, "title").send_keys("Ingenieria parte I")

import time

print('esperaremos 3 segundos' )

time.sleep(3)

driver.find_element(By.NAME, "year").click()

driver.find_element(By.NAME, "year").send_keys("2022")

print('esperaremos 3 segundos' )

time.sleep(3)

driver.find_element(By.NAME, "director").click()

driver.find_element(By.NAME, "director").send_keys("Pepito Paga-doble")

print('esperaremos 3 segundos' )

time.sleep(3)

driver.find_element(By.NAME, "rating").click()

driver.find_element(By.NAME, "rating").send_keys("4")

print('esperaremos 3 segundos' )

time.sleep(3)

driver.find_element(By.CSS_SELECTOR, ".btn").click()

print('esperaremos 3 segundos' )

time.sleep(3)

driver.find_element(By.ID, "add-movie").click()

print('esperaremos 3 segundos' )

time.sleep(3)

 

driver.find_element(By.NAME, "title").click()

driver.find_element(By.NAME, "title").send_keys("Ingenieria la Venganza")

print('esperaremos 3 segundos' )

time.sleep(3)

driver.find_element(By.NAME, "year").click()

driver.find_element(By.NAME, "year").send_keys("2023")

print('esperaremos 3 segundos' )

time.sleep(3)

driver.find_element(By.NAME, "director").click()

driver.find_element(By.NAME, "director").send_keys("Juanito Perez")

print('esperaremos 3 segundos' )

time.sleep(3)

driver.find_element(By.NAME, "rating").click()

driver.find_element(By.NAME, "rating").send_keys("5")

print('esperaremos 3 segundos' )

time.sleep(3)

driver.find_element(By.CSS_SELECTOR, ".btn").click()

print('esperaremos 3 segundos' )

time.sleep(3)

input1 = "Mala, la pelicula"

driver.get("+input1+")

time.sleep(5)

input2 = "La mejor pelicula que he visto!!"

driver.get("+input2+")

time.sleep(5)
