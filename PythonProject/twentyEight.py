import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://demoqa.com/text-box")
driver.find_element(By.ID, "userName").send_keys("Qudsia Omama")
driver.find_element(By.ID, "userEmail").send_keys("Se22F-002@ssuet.edu.pk")
driver.find_element(By.ID, "currentAddress").send_keys("Jauhar")
driver.find_element(By.ID, "permanentAddress").send_keys("As above")
driver.find_element(By.ID, "submit").click()
time.sleep(2)
