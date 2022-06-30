import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://jahidpqa.wordpress.com/")
driver.maximize_window()

driver.find_element(By.XPATH, "//a[contains(text(),'Contact Us')]").click()
driver.find_element(By.ID, "g13-name").send_keys("Test Data")
driver.find_element(By.ID, "g13-email").send_keys("abc@mail.com")
driver.find_element(By.ID, "contact-form-comment-g13-message").send_keys("This is a simple test")
driver.find_element(By.XPATH, "//button[contains(text(),'Contact Us')]").click()
print(driver.current_url)

success_message = driver.find_element(By.ID, "contact-form-13").text
print(success_message)

driver.find_element(By.XPATH, "//a[contains(text(),'go back')]").click()
print(driver.current_url)

time.sleep(3)
driver.quit()
