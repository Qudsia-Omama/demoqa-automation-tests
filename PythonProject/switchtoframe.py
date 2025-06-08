import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://demoqa.com/frames")
driver.switch_to.frame("frame1")
assert "This is a sample page" in driver.page_source
driver.switch_to.default_content()
print("Frame1 executed successfully")
time.sleep(2)
driver.execute_script("window.scrollTo(0, 500)")
time.sleep(1)
driver.switch_to.frame("frame2")
assert "This is a sample page" in driver.page_source
print("Frame2 executed successfully")
time.sleep(2)

