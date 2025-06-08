import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://demoqa.com/modal-dialogs")
driver.maximize_window()
mainMenu = driver.find_element(By.XPATH,
    "//body/div[@id='app']/div[contains(@class,'body-height')]/div[contains(" +
    "@class,'container playgound-body')]/div[contains(@class,'row')]/div[" +
    "contains(@class,'col-md-3')]/div[contains(@class,'left-pannel')]/div[" +
    "contains(@class,'accordion')]/div[1]/span[1]/div[1]"
)
subMenu = driver.find_element(By.ID, "item-0")
action = ActionChains(driver)
action.move_to_element(mainMenu).click().perform()
action.move_to_element(subMenu).click().perform()
print("THE END")
time.sleep(6)
driver.quit()
