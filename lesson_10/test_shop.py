from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pages.metod_shop import Avtoriz_form
from pages.metod_shop import Shop_form
from pages.metod_shop import Basket_form
from pages.metod_shop import Your_information
import allure


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


@allure.severity("blocker")
@allure.title("Авторизация на сайте")
@allure.description("Проверка формы авторизации")
@allure.feature("Авторизация")
def test_shop_avtoriz():
    with allure.step("Иницилизация класса авторизации"):
        avtoriz_form = Avtoriz_form(driver)
        with allure.step("Ввод имени пользователя"):
            avtoriz_form.user_name("standard_user")
        with allure.step("Ввод пароля пользователя"):
            avtoriz_form.password("secret_sauce")
        with allure.step("Нажатие на кнопку"):
            avtoriz_form.click_form()

@allure.severity("blocker")
@allure.title("Работа каталога")
@allure.description("Товар складывается в корзину")
@allure.feature("Корзина")
def test_shop_form():
    with allure.step("Иницилизация класса магазин"):
        shop_form = Shop_form(driver)
    with allure.step("Кладем товар в корзину и нажимаем кнопку"):
        shop_form.basket()

@allure.severity("blocker")
@allure.title("Работа корзины")
@allure.description("Товар отображается в корзине")
@allure.feature("Корзина")
def test_shop_basket():
    with allure.step("Иницилизация класса корзина"):
        basket_form = Basket_form(driver)
    with allure.step("Нажатие кнопки checkout"):
        basket_form.checkout()

@allure.severity("blocker")
@allure.title("Проверка итоговой суммы покупки")
@allure.description("Итоговая сумма покупок отображается верно")
@allure.feature("Итоговая сумма")
def test_shop_info():
    with allure.step("Иницилизация класса информация"):
        your_information = Your_information(driver)
        with allure.step("Ввод имени в форму"):
            your_information.first_name("Nastia")
        with allure.step("Ввод фамилии в форму"):
            your_information.last_name("St")
        with allure.step("Ввод индекса в форму"):
            your_information.postal_code("650405")
    with allure.step("Нажатие на кнопку"):
        your_information.click_form_info()
    with allure.step("Проверка, что итоговая сумма равна 58.29"):
        with allure.step("Находим элемент с итоговой суммой"):
            total_price = driver.find_element(By.CSS_SELECTOR, ".summary_total_label")
        with allure.step("Получаем информацию о итоговой сумме"):
            total = total_price.text.strip().replace("Total: $", "")
            expected_total = "58.29"
        with allure.step("Сравниваем информацию с суммой"):
            assert total == expected_total
    driver.quit()