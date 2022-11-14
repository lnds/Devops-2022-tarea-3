import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)

driver.get("http://localhost:8080/")

driver.find_element(By.ID, "add-movie").click()
driver.find_element(By.NAME, "title").send_keys("RoboCop")
driver.find_element(By.NAME, "year").send_keys("1987")
driver.find_element(By.NAME, "director").send_keys("Paul Verhoeven")
driver.find_element(By.NAME, "rating").send_keys("7.6")    
driver.find_element(By.NAME, "review").send_keys("En una Detroit distópica y asolada por el crimen, un policía herido de muerte regresa al servicio como un poderoso cyborg atormentado por sus antiguos recuerdos.")
driver.find_element(By.CSS_SELECTOR, ".btn").click()

time.sleep(2)

driver.find_element(By.ID, "add-movie").click()
driver.find_element(By.NAME, "title").send_keys("3 Idiots")
driver.find_element(By.NAME, "year").send_keys("2009")
driver.find_element(By.NAME, "director").send_keys("Rajkumar Hirani")
driver.find_element(By.NAME, "rating").send_keys("8.4")    
driver.find_element(By.NAME, "review").send_keys("Dos amigos buscan a su compañero perdido. Recuerdan sus días de universidad y como su amigo les inspiró a pensar de forma diferente, incluso cuando el resto del mundo los llamó idiotas.")
driver.find_element(By.CSS_SELECTOR, ".btn").click()

time.sleep(2)

driver.find_element(By.LINK_TEXT, "Dune").click()
driver.find_element(By.NAME, "review").clear()
driver.find_element(By.NAME, "review").send_keys("Gran adaptación de la novela clásica de ciencia ficción")
driver.find_element(By.CSS_SELECTOR, ".btn").click()

time.sleep(2)

driver.find_element(By.LINK_TEXT, "Elvis").click()
driver.find_element(By.NAME, "review").clear()
driver.find_element(By.NAME, "review").send_keys("Película biográfica del rey del rock")
driver.find_element(By.CSS_SELECTOR, ".btn").click()

time.sleep(10)