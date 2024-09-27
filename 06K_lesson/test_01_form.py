from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(20)
driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")


driver.find_element(By.CSS_SELECTOR, '[name="first-name"]').send_keys("Иван")
driver.find_element(By.CSS_SELECTOR, '[name="last-name"]').send_keys("Петров")
driver.find_element(By.CSS_SELECTOR, '[name="address"]').send_keys("Ленина, 55-3")
driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]').send_keys("test@skypro.com")
driver.find_element(By.CSS_SELECTOR, '[name="phone"]').send_keys("+7985899998787")
driver.find_element(By.CSS_SELECTOR, '[name="city"]').send_keys("Москва")
driver.find_element(By.CSS_SELECTOR, '[name="country"]').send_keys("Россия")
driver.find_element(By.CSS_SELECTOR, '[name="job-position"]').send_keys("QA")
driver.find_element(By.CSS_SELECTOR, '[name="company"]').send_keys("SkyPro")
driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
red = driver.find_element(By.CSS_SELECTOR, "#zip-code").value_of_css_property("background-color")
green = driver.find_element(By.CSS_SELECTOR, "#first-name").value_of_css_property("background-color")
assert "danger" in driver.find_element(By.CSS_SELECTOR, "#zip-code").get_attribute("class")
assert "success" in driver.find_element(By.CSS_SELECTOR, "#first-name").get_attribute("class")
assert "success" in driver.find_element(By.CSS_SELECTOR, "#last-name").get_attribute("class")
assert "success" in driver.find_element(By.CSS_SELECTOR, "#address").get_attribute("class")
assert "success" in driver.find_element(By.CSS_SELECTOR, "#e-mail").get_attribute("class")
assert "success" in driver.find_element(By.CSS_SELECTOR, "#phone").get_attribute("class")
assert "success" in driver.find_element(By.CSS_SELECTOR, "#city").get_attribute("class")
assert "success" in driver.find_element(By.CSS_SELECTOR, "#country").get_attribute("class")
assert "success" in driver.find_element(By.CSS_SELECTOR, "#job-position").get_attribute("class")
assert "success" in driver.find_element(By.CSS_SELECTOR, "#company").get_attribute("class")
print(red)
print(green)
driver.quit()
