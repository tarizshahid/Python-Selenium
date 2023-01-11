import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://www.youtube.com")
time.sleep(10)
driver.find_element(By.XPATH, "//input[@id='search']").send_keys("Tariz Evilbot Shahid")
driver.find_element(By.XPATH, "//input[@id='search']").send_keys(Keys.RETURN)

time.sleep(10)



driver.close()