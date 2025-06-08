import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://demoqa.com/selectable")
btn1 = driver.find_element(By.XPATH, "//*[@id='verticalListContainer']/li[1]")
btn2 = driver.find_element(By.XPATH, "//*[@id='verticalListContainer']/li[2]")
btn3 = driver.find_element(By.XPATH, "//*[@id='verticalListContainer']/li[3]")
btn4 = driver.find_element(By.XPATH, "//*[@id='verticalListContainer']/li[4]")
action = ActionChains(driver)
action.click(btn1).perform()
time.sleep(1)
action.click(btn2).perform()
time.sleep(1)
action.click(btn3).perform()
time.sleep(1)
action.click(btn4).perform()
time.sleep(2)


