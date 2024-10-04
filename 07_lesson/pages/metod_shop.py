from selenium.webdriver.common.by import By


driver = None


class Avtoriz_form:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com")
        self.driver.implicitly_wait(20)

    def user_name(self, user_name):
        self.driver.find_element(By.ID, "user-name").send_keys(user_name)

    def password(self, password):
        self.driver.find_element(By.ID, "password").send_keys(password)

    def click_form(self):
        self.driver.find_element(By.ID, "login-button").click()


class Shop_form:
    def __init__(self, driver):
        self.driver = driver

    def basket(self):
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
        self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()


class Basket_form:
    def __init__(self, driver):
        self.driver = driver

    def checkout(self):
        self.driver.find_element(By.ID, "checkout").click()


class Your_information:
    def __init__(self, driver):
        self.driver = driver

    def first_name(self, first_name):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)

    def last_name(self, last_name):
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)

    def postal_code(self, postal_code):
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)

    def click_form_info(self):
        self.driver.find_element(By.ID, "continue").click()
