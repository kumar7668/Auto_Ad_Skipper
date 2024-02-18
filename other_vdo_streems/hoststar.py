from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])

driver = webdriver.Chrome(options=options)
action = ActionChains(driver)
driver.maximize_window()
driver.get("https://www.hotstar.com/ca")
driver.find_element(By.XPATH, '//*[@id="page-container"]/div/div[2]/aside/nav/div[1]/a/button').click()
print("chala bhai")
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="page-container"]/div/div[3]/div[1]/div/div[3]/div/button').click()
time.sleep(5)
print("pass1")
driver.find_element(By.XPATH, '//*[@id="7"]').click()
time.sleep(5)
print("pass2")
driver.find_element(By.NAME, "email").send_keys("sonukumar")  # Use By.NAME
driver.find_element(By.NAME, "password").send_keys("sonu0000")  # Use By.NAME
print("pass")
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div[3]/div/div/div[1]/div/div[2]/div/div[1]/div/div/form/button").click()
time.sleep(5)
driver.find_element_by_id("searchField").send_keys("Starplus")
time.sleep(5)
driver.get("https://www.hotstar.com/in/channels/starplus")
time.sleep(3)
# serial hover
serial = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[1]/div[2]/div/div/div/div/div/div/div[7]/div/article/a")
action.move_to_element(serial).perform()
# click on tile
driver.find_element_by_xpath("/html/body/div/div[2]/div/div[1]/div[2]/div/div/div/div/div/div/div[7]/div/article/a/div[2]/span").click()
time.sleep(2)
# click play
driver.find_element_by_xpath("/html/body/div/div[2]/div/div[1]/div[2]/div[1]/div/div[3]/div[2]/a").click()
# fullscreen
ActionChains(driver).key_down(Keys.CONTROL).send_keys('f').key_up(Keys.CONTROL).perform()
