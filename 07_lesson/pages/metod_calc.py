from selenium.webdriver.common.by import By


driver = None


class Calc_form:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def delay(self, delay):
        self.driver.find_element(By.ID, "delay").clear()
        self.driver.find_element(By.ID, "delay").send_keys(delay)

    def click_form(self):
        self.driver.find_element(By.XPATH, "//span[text() = '7']").click()
        self.driver.find_element(By.XPATH, "//span[text() = '+']").click()
        self.driver.find_element(By.XPATH, "//span[text() = '8']").click()
        self.driver.find_element(By.XPATH, "//span[text() = '=']").click()
