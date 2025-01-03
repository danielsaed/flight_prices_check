from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
from pyvirtualdisplay import Display
import os
import time
import undetected_chromedriver as uc
import random
from fake_useragent import UserAgent


def use_xpath(xpath,time):
    return WebDriverWait(driver, time).until(EC.presence_of_element_located((By.XPATH, xpath)))
    

display = Display(visible=0, size=(800, 800))  
display.start()

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
ua = UserAgent()
user_agent = ua.random

chrome_options = uc.ChromeOptions()
chrome_options.add_argument(f"user-agent={user_agent}")

options = [
    #"--headless",  # Hides the browser window
    "--window-size=1200,1200",
    "--ignore-certificate-errors",
    "--lang=es",
    "--disable-dev-shm-usage",  # Overcome limited resource problems
    "--no-sandbox",  # Bypass OS security model
    #"--disable-gpu",  # Applicable to windows os only
    #"--disable-extensio+ns",  # Disable extensions
    #"--remote-debugging-port=9222"  # Enable remote debugging
]

for option in options:
    chrome_options.add_argument(option)

driver = uc.Chrome(options=chrome_options)

driver.get(r'https://www.expedia.mx/Flights-Search?flight-type=on&mode=search&trip=oneway&leg1=from:Tepic,%20Nayarit,%20M%C3%A9xico,to:Ciudad%20de%20M%C3%A9xico,%20M%C3%A9xico%20(MEX-Aeropuerto%20Internacional%20de%20la%20Ciudad%20de%20M%C3%A9xico),departure:14/01/2025TANYT,fromType:CITY,toType:AIRPORT&options=cabinclass:economy&fromDate=14/01/2025&d1=2025-1-14&passengers=adults:1,infantinlap:N')

quantity_flights= 0

use_xpath("//li[@data-test-id='offer-listing'][1]//div/button/span",180)

try:
  while True:
      
      price = use_xpath(f"//li[@data-test-id='offer-listing'][{quantity_flights+1}]/div/div/div/div/div[1]/div[2]/div/div/section/span",2)
      tiempo = use_xpath(f"//li[@data-test-id='offer-listing'][{quantity_flights+1}]/div/div/div/div/div[1]/div[1]/div/div[2]/div",2)
      use_xpath(f"//li[@data-test-id='offer-listing'][{quantity_flights+1}]//div/button/span",2)
      use_xpath(f"//li[@data-test-id='offer-listing'][{quantity_flights+1}]//div/button/span",2)
      quantity_flights += 1
      
finally:
    print(f"Se encontraron {quantity_flights} vuelos")

vuelos = use_xpath("//li[@data-test-id='offer-listing'][1]//div/button/span",60)
# precio //li[@data-test-id='offer-listing'][1]/div/div/div/div/div[1]/div[2]/div/div/section/span
# all info //li[@data-test-id='offer-listing'][1]//div/button/span
# tiempo y tipo de vuelo //li[@data-test-id='offer-listing'][1]/div/div/div/div/div[1]/div[1]/div/div[2]/div
# aerolinea //li[@data-test-id='offer-listing'][1]/div/div/div/div/div[1]/div[1]/div/div[3]/div[2]
# horario //li[@data-test-id='offer-listing'][1]/div/div/div/div/div[1]/div[1]/div/div[1]/div[2]

print(vuelos.text)
time.sleep(5)

'''vuelos = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="multi-product-search-form-1"]/div/div/div/div/div[1]/ul/li[2]/a/span'))).click()

#time.sleep(30)

viaje_sencillo = driver.find_element(By.XPATH,"//span[normalize-space()='Viaje sencillo']").click()
time.sleep(.5)
origen = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//button[@aria-label='Origen']"))).click()
time.sleep(.5)
tepic = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//input[@id='origin_select']"))).send_keys("Tepic")
time.sleep(.5)
select_tepic = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//button[@aria-label='Tepic (TPQ - A. Nacional Amado Nervo) Nayarit, México']"))).click()
time.sleep(.5)
destino = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//button[@aria-label='Destino']"))).click()
time.sleep(.5)
destino_select = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//input[@id='destination_select']"))).send_keys("Ciudad de México")
time.sleep(.5)
destino_select = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//button[@aria-label='Ciudad de México (MEX - Aeropuerto Internacional de la Ciudad de México) México']"))).click()
time.sleep(.5)
destino_select = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//input[@id='destination_select']"))).click()
time.sleep(.5)
destino_select = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//input[@id='destination_select']"))).click()
time.sleep(.5)
input()'''

#xpath viaje sencillo //span[normalize-space()='Viaje sencillo']
#xpath boton origen //button[@aria-label='Origen']
#xpath input origen //input[@id='origin_select']
#xpath tepic //button[@aria-label='Tepic (TPQ - A. Nacional Amado Nervo) Nayarit, México']

#xpath boton destino //button[@aria-label='Destino']
#xpath input destino //input[@id='destination_select']
#xpath cdmx //button[@aria-label='Ciudad de México (MEX - Aeropuerto Internacional de la Ciudad de México) México']
#xpath date //button[@data-testid="uitk-date-selector-input1-default"]/following-sibling::input
#xpath date input //button[@data-testid="uitk-date-selector-input1-default"]/preceding::input[1]
#xpath search //button[@id='search_button']
#xpath wait to //select[@id='sort-filter-dropdown-SORT']

#xpath listings //li[@data-test-id='offer-listing']

#path text of the listing //li[@data-test-id='offer-listing'][1]//div/button/span

with open('./GitHub_Action_Results.txt', 'w') as f:
    f.write(f"This was written with a GitHub action {driver.title}")
print('DONE')

driver.close()