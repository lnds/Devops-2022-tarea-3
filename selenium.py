rom selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)
driver.get('http:/localhost:8080')

driver.find_element(By.ID, "add-movie").click()

driver.find_element(By.NAME, "title").send_keys("Dragon ball:Super hero")
driver.find_element(By.NAME, "year").send_keys("2022")
driver.find_element(By.NAME, "director").send_keys("Tetsuro Kodama")
driver.find_element(By.NAME, "rating").send_keys("3.7")
driver.find_element(By.NAME, "review").send_keys("La malvada organización Red Ribbon Army se reforma con nuevos y más poderosos androides, Gamma 1 y Gamma 2 para buscar venganza.")

driver.find_element(By.CLASS_NAME, "btn-primary").send_keys(Keys.ENTER)

time.sleep(5)

driver.find_element(By.ID, "add-movie").click()

driver.find_element(By.NAME, "title").send_keys("Los juegos del hambre")
driver.find_element(By.NAME, "year").send_keys("2012")
driver.find_element(By.NAME, "director").send_keys("Francis Lawrence, Gary Ross")
driver.find_element(By.NAME, "rating").send_keys("7.2")
driver.find_element(By.NAME, "review").send_keys("Katniss Everdeen toma voluntariamente el lugar de su hermana menor en los Juegos del Hambre: una competencia televisada en la que dos adolescentes de cada uno de los doce distritos de Panem son elegidos al azar para luchar hasta la muerte.")

driver.find_element(By.CLASS_NAME, "btn-primary").send_keys(Keys.ENTER)

time.sleep(5)

driver.find_element(by=By.XPATH, value="//a[@href='/edit/1']").click()
driver.find_element(By.NAME, "review").clear()
driver.find_element(By.NAME, "review").send_keys("Gran adaptación de una novela clásica de ciencia ficción.")
driver.find_element(By.CLASS_NAME, "btn-primary").send_keys(Keys.ENTER)

time.sleep(5)

driver.find_element(by=By.XPATH, value="//a[@href='/edit/2']").click()
driver.find_element(By.NAME, "review").clear()
driver.find_element(By.NAME, "review").send_keys("Emocionante película biográfica estilizada del Rey.")
driver.find_element(By.CLASS_NAME, "btn-primary").send_keys(Keys.ENTER)

driver.quit()