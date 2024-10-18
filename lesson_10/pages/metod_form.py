from selenium.webdriver.common.by import By

driver = None


class Fil_form:
    """
        Этот класс предназначен для сбора всех необходимых данных в консоль и их отправки по нажатию кнопки
    """
    def __init__(self, driver):
        """
        Этот метод предназначен для открытия страницы браузера
        """
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self.driver.implicitly_wait(4)

    def first_name(self, first_name: str) -> str:
        """
        Этот метод предназначен для ввода имени в консоль
        """
        self.driver.find_element(By.CSS_SELECTOR, '[name="first-name"]').send_keys(first_name)

    def last_name(self, last_name: str) -> str:
        """
        Этот метод предназначен для ввода фамилии в консоль
        """
        self.driver.find_element(By.CSS_SELECTOR, '[name="last-name"]').send_keys(last_name)

    def address(self, address: str) -> str:
        """
        Этот метод предназначен для ввода адреса в консоль
        """
        self.driver.find_element(By.CSS_SELECTOR, '[name="address"]').send_keys(address)

    def e_mail(self, e_mail: str) -> str:
        """
        Этот метод предназначен для ввода электронного адреса в консоль
        """
        self.driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]').send_keys(e_mail)

    def phone(self, phone: int) -> int:
        """
        Этот метод предназначен для ввода телефона в консоль
        """
        self.driver.find_element(By.CSS_SELECTOR, '[name="phone"]').send_keys(phone)

    def city(self, city: str) -> str:
        """
        Этот метод предназначен для ввода города в консоль
        """
        self.driver.find_element(By.CSS_SELECTOR, '[name="city"]').send_keys(city)

    def country(self, country: str) -> str:
        """
        Этот метод предназначен для ввода страны в консоль
        """
        self.driver.find_element(By.CSS_SELECTOR, '[name="country"]').send_keys(country)

    def job_position(self, job_position: str) -> str:
        """
        Этот метод предназначен для ввода должности в консоль
        """
        self.driver.find_element(By.CSS_SELECTOR, '[name="job-position"]').send_keys(job_position)

    def company(self, company: str) -> str:
        """
        Этот метод предназначен для ввода компании в консоль
        """
        self.driver.find_element(By.CSS_SELECTOR, '[name="company"]').send_keys(company)

    def click_form(self):
        """
        Этот метод предназначен для нажатия кнопки отправить
        """
        self.driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
