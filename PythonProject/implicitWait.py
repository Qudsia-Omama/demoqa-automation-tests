from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demoqa.com/accordian")

btn1 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "section1Heading"))
)
btn1.click()
time.sleep(2)

btn2 = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.ID, "section2Heading"))
)
btn2.click()
time.sleep(2)

btn3 = driver.find_element(By.ID, "section3Heading")
driver.execute_script("arguments[0].click()", btn3)

time.sleep(2)
driver.close()
driver.quit()
