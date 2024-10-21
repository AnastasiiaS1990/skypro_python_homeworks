from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.metod_calc import Calc_form
import allure


@allure.severity("critical")
@allure.title("Работа калькулятора")
@allure.feature("Калькулятор")
@allure.description("Тест вводит секунды ожидания ответа от калькулятора и выполняет математические операции")
def test_calcul():
    with allure.step("Открыть страницу калькулятор"):
        driver = webdriver.Chrome()
    with allure.step("Иницилизация класса калькулятор"):
        form = Calc_form(driver)
    with allure.step("Ввести значение ожидания от калькулятора"):
        form.delay("15")
    with allure.step("Ввести кнопками математические значения и нажать равно "):
        form.click_form()
    with allure.step("Найти на странице элемент с результатом ожидания"):
        WebDriverWait(driver, 16).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))
        with allure.step("Взять информацию о сумме введенного ожидания"):
            result_text = driver.find_element(By.CLASS_NAME, "screen").text
        with allure.step("Проверить, что введенное значение равняется значению в строке"):
            assert result_text == "15"
    driver.quit()
