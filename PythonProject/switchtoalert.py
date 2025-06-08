import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demoqa.com/alerts")
driver.maximize_window()

driver.find_element(By.ID, "alertButton").click()
time.sleep(5)
driver.switch_to.alert.accept()

driver.find_element(By.ID, "timerAlertButton")
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "timerAlertButton"))
).click()
time.sleep(6)
driver.switch_to.alert.accept()

driver.find_element(By.ID, "confirmButton").click()
driver.switch_to.alert.dismiss()
time.sleep(6)

try:
    assert "You selected Cancel" in driver.page_source
except:
    assert "You selected Ok" in driver.page_source

driver.find_element(By.ID, "promtButton").click()
driver.switch_to.alert.send_keys("Qudsia" + Keys.ENTER)

time.sleep(6)
