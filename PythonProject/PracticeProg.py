import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://demoga.com/text-box")
driver.maximize_window()
driver.find_element(By.ID,"userName").send_keys("Qudsia")
print(driver.title)
print(driver.current_url)
time.sleep(2)
