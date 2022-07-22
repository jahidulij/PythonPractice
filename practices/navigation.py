import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://jahidpqa.wordpress.com/")
driver.maximize_window()

print(driver.current_url)
driver.find_element(By.XPATH, "//a[contains(text(),'Content Migration')]").click()
print(driver.current_url)
driver.find_element(By.XPATH, "//a[contains(text(),'Testing Capabilities')]").click()
print(driver.current_url)
driver.find_element(By.XPATH, "//a[contains(text(),'About')]").click()
print(driver.current_url)
driver.find_element(By.XPATH, "//a[contains(text(),'Contact Us')]").click()
print(driver.current_url)
driver.find_element(By.XPATH, "//a[contains(text(),'Home')]").click()
print(driver.current_url)
driver.find_element(By.XPATH, "//a[contains(text(),'Get in Touch')]").click()
print(driver.current_url)

time.sleep(3)
driver.quit()
