from selenium.webdriver.common.by import By


driver = None


class Fil_form:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self.driver.implicitly_wait(4)

    def first_name(self, first_name):
        self.driver.find_element(By.CSS_SELECTOR, '[name="first-name"]').send_keys(first_name)

    def last_name(self, last_name):
        self.driver.find_element(By.CSS_SELECTOR, '[name="last-name"]').send_keys(last_name)

    def address(self, address):
        self.driver.find_element(By.CSS_SELECTOR, '[name="address"]').send_keys(address)

    def e_mail(self, e_mail):
        self.driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]').send_keys(e_mail)

    def phone(self, phone):
        self.driver.find_element(By.CSS_SELECTOR, '[name="phone"]').send_keys(phone)

    def city(self, city):
        self.driver.find_element(By.CSS_SELECTOR, '[name="city"]').send_keys(city)

    def country(self, country):
        self.driver.find_element(By.CSS_SELECTOR, '[name="country"]').send_keys(country)

    def job_position(self, job_position):
        self.driver.find_element(By.CSS_SELECTOR, '[name="job-position"]').send_keys(job_position)

    def company(self, company):
        self.driver.find_element(By.CSS_SELECTOR, '[name="company"]').send_keys(company)

    def click_form(self):
        self.driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
