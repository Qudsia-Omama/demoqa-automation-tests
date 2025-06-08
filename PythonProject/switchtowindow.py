import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://demoqa.com/browser-windows")
wait = WebDriverWait(driver, 10)
tab_button = wait.until(EC.element_to_be_clickable((By.ID, "tabButton")))
driver.execute_script("arguments[0].click();", tab_button)
driver.switch_to.window(driver.window_handles[1])
assert "This is a sample page" in driver.page_source
time.sleep(2)
driver.switch_to.window(driver.window_handles[0])
window_button = wait.until(EC.element_to_be_clickable((By.ID, "windowButton")))
driver.execute_script("arguments[0].click();", window_button)
driver.switch_to.window(driver.window_handles[2])
assert "This is a sample page" in driver.page_source
time.sleep(2)

