from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(20)
driver.get("https://www.saucedemo.com")


driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
driver.find_element(By.ID, "checkout").click()
driver.find_element(By.ID, "first-name").send_keys("Nastia")
driver.find_element(By.ID, "last-name").send_keys("St")
driver.find_element(By.ID, "postal-code").send_keys("650405")
driver.find_element(By.ID, "continue").click()
total_price = driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text
print(total_price)
driver.quit()
