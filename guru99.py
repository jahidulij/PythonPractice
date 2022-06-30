import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
url = "https://www.demo.guru99.com/V4/index.php"

driver.get(url)
driver.maximize_window()
driver.find_element(By.NAME, "uid").send_keys("mngr421447")
driver.find_element(By.NAME, "password").send_keys("pEquhar")
driver.find_element(By.NAME, "btnLogin").click()
# driver.find_element(By.NAME, "btnReset").click()



time.sleep(3)
