from selenium.webdriver.common.by import By


driver = None


class Avtoriz_form:
    """
        Этот класс предназначен для авторизации на сайте
    """
    def __init__(self, driver):
        """
        Этот метод предназначен для открытия страницы браузера и ожидания 20 сек
        """
        self.driver = driver
        self.driver.get("https://www.saucedemo.com")
        self.driver.implicitly_wait(20)

    def user_name(self, user_name: str) -> str:
        """
        Этот метод предназначен для ввода имени пользователя в консоль
        """
        self.driver.find_element(By.ID, "user-name").send_keys(user_name)

    def password(self, password: str) -> str:
        """
        Этот метод предназначен для ввода пароля в консоль
        """
        self.driver.find_element(By.ID, "password").send_keys(password)

    def click_form(self):
        """
        Этот метод предназначен для нажатия кнопки войти
        """
        self.driver.find_element(By.ID, "login-button").click()


class Shop_form:
    """
        Этот класс предназначен для выбора товаров на сайте
    """
    def __init__(self, driver):
        self.driver = driver

    def basket(self):
        """
        Этот метод кладет необходимые товары в корзину и осуществляет переход в нее
        """
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
        self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()


class Basket_form:
    """
        Этот класс предназначен для проверки товаров в корзине и перехода на этап ввода данных покупателя
    """
    def __init__(self, driver):
        self.driver = driver

    def checkout(self):
        """
        Этот метод осуществляет переход из корзины на форму для ввода дданых покупателя 
        """
        self.driver.find_element(By.ID, "checkout").click()


class Your_information:
    """
        Этот класс предназначен для ввода данных покупателя
    """
    def __init__(self, driver):
        self.driver = driver

    def first_name(self, first_name: str) -> str:
        """
        Этот метод предназначен для ввода имени в консоль
        """
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)

    def last_name(self, last_name: str) -> str:
        """
        Этот метод предназначен для ввода фамилии в консоль
        """
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)

    def postal_code(self, postal_code: int) -> int:
        """
        Этот метод предназначен для ввода индекса в консоль
        """
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)

    def click_form_info(self):
        """
        Этот метод осуществляет переход на форму со счетом для оплаты 
        """
        self.driver.find_element(By.ID, "continue").click()
