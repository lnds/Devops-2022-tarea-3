from traceback import print_list
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
import googletrans
from selenium.webdriver.support import expected_conditions as EC
import time

#configuracion driver y chrome desde linux mint
# nos aseguramos que la version de chromedriver aguante la version de chrome
driver_location = '/usr/bin/chromedriver'
binary_location = '/usr/bin/google-chrome'

#traducimos el texto todos las clases .review
#iniciamos googletrans , sudo pipe3 install googletrans 4.0.0rc1
translator = googletrans.Translator()

options = webdriver.ChromeOptions()
options.binary_location = binary_location

driver = webdriver.Chrome(executable_path=driver_location,options=options)

#mi contexto local
driver.get("http://127.0.0.1:8080/")


#agregamos las 2 peliculas.
driver.find_element(By.ID, "add-movie").click()
driver.find_element(By.NAME, "title").send_keys("Irreversible")
driver.find_element(By.NAME, "year").send_keys("2022")
driver.find_element(By.NAME, "director").send_keys("Gaspar Noé")
driver.find_element(By.NAME, "rating").send_keys("5")
driver.find_element(By.NAME,"review").send_keys("Contada en orden cronológico inverso, narra la búsqueda emprendida por dos hombres, Marcus y Pierre, quienes desean vengar la brutal violación de Alex, novia de Marcus y exnovia de Pierre.")
driver.find_element(By.CSS_SELECTOR, ".btn").click()

driver.find_element(By.ID, "add-movie").click()
driver.find_element(By.NAME, "title").send_keys("Requiem for a Dream")
driver.find_element(By.NAME, "year").send_keys("2000")
driver.find_element(By.NAME, "director").send_keys("Darren Aronofsky")
driver.find_element(By.NAME, "rating").send_keys("5")
driver.find_element(By.NAME,"review").send_keys("Cuenta la historia de Harry Goldfarb (Jared Leto), su madre Sara Goldfarb (Ellen Burstyn), su novia Marion Silver (Jennifer Connelly) y su amigo Tyrone C. Love (Marlon Wayans). La historia se divide en tres estaciones: verano, otoño e invierno.")
driver.find_element(By.CSS_SELECTOR, ".btn").click()

nums = [1, 2] #identidicadores de las peliculas para traducir
#contatenamos la id de las peliculas y traducimos su review
#finalmente guardamos.
for n in nums:
    url = "/edit/"+str(n)
    driver.find_element(By.XPATH,'//a[@href="'+url+'"]').click()
    txtAreaReview = driver.find_element(By.NAME, "review")
    txtAreaReview.clear()
    txtAreaReview.send_keys(translator.translate(txtAreaReview.text,dest='es').text)
    driver.find_element(By.CSS_SELECTOR, ".btn").click()

driver.quit()