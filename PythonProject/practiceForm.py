import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://demoqa.com/automation-practice-form")

driver.find_element(By.ID, "firstName").clear()
driver.find_element(By.ID, "firstName").send_keys("Qudsia")
driver.find_element(By.ID, "lastName").clear()
driver.find_element(By.ID, "lastName").send_keys("Omama")
driver.find_element(By.XPATH, "//*[@id='userEmail']").clear()
driver.find_element(By.XPATH, "//*[@id='userEmail']").send_keys("Se22F-002@ssuet.edu.pk")
driver.find_element(By.XPATH, "//label[@for='gender-radio-2']").click()
driver.find_element(By.ID, "userNumber").clear()
driver.find_element(By.ID, "userNumber").send_keys("0300026345")

dd = driver.find_element(By.ID, "dateOfBirthInput")
driver.execute_script("arguments[0].click()", dd)
dob = driver.find_element(By.ID, "dateOfBirthInput")
dob.clear()
dob.send_keys("12 Dec 1995")
dob.send_keys(Keys.ENTER)

driver.find_element(By.ID, "subjectsInput").send_keys("ENGLISH")
driver.find_element(By.ID, "subjectsInput").send_keys(Keys.ENTER)

hobbies = driver.find_element(By.XPATH, "//*[@id='hobbiesWrapper']/div[2]/div[2]/label")
driver.execute_script("arguments[0].click()", hobbies)
driver.find_element(By.ID, "uploadPicture").send_keys("C:/Users/huawei/Downloads/test.jpg")
driver.find_element(By.ID, "currentAddress").send_keys("Jauhar")

time.sleep(2)

select = driver.find_element(By.XPATH, "//*[@id='stateCity-label']")
driver.execute_script("arguments[0].click()", select)
Dropdown = driver.find_element(By.XPATH, "//*[@id='state']/div/div[1]/div[1]")
driver.execute_script("arguments[0].click()", Dropdown)

submit = driver.find_element(By.ID, "submit")
driver.execute_script("arguments[0].click()", submit)

time.sleep(5)
