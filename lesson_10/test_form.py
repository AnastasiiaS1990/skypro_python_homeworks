from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.metod_form import Fil_form
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import allure


@allure.severity("critical")
@allure.title("Работа формы с информацией")
@allure.feature("Форма с информацией")
@allure.description("Тест предназначен для сбора всех необходимых данных в консоль и их отправки по нажатию кнопки")
def test_from():
    with allure.step("Открыть страницу с формой"):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    with allure.step("Иницилизация класса форма"):
        form = Fil_form(driver)
    with allure.step("Ввод имени в форму"):
        form.first_name("Иван")
    with allure.step("Ввод фамилии в форму"):
        form.last_name("Петров")
    with allure.step("Ввод адреса в форму"):
        form.address("Ленина, 55-3")
    with allure.step("Ввод e-mail в форму"):
        form.e_mail("test@skypro.com")
    with allure.step("Ввод телефона в форму"):
        form.phone("+7985899998787")
    with allure.step("Ввод города в форму"):
        form.city("Москва")
    with allure.step("Ввод страны в форму"):
        form.country("Россия")
    with allure.step("Ввод должности в форму"):
        form.job_position("QA")
    with allure.step("Ввод компании в форму"):
        form.company("SkyPro")
    with allure.step("Нажатие на кнопку"):
        form.click_form()
    with allure.step("Проверяем, что не заполненное поле подсвечивается красным (danger), а заполненное зеленым (success)"):
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
    driver.quit()
