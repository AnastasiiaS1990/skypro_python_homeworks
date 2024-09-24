from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 46)
driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
driver.find_element(By.ID, "delay").clear()
driver.find_element(By.ID, "delay").send_keys("45")
driver.find_element(By.XPATH, "//span[text() = '7']").click()
driver.find_element(By.XPATH, "//span[text() = '+']").click()
driver.find_element(By.XPATH, "//span[text() = '8']").click()
driver.find_element(By.XPATH, "//span[text() = '=']").click()
wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))
result_text = driver.find_element(By.CLASS_NAME, "screen").text
assert result_text == "15"
driver.quit()
