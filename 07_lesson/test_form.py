from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.metod_form import Fil_form
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_from():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    form = Fil_form(driver)
    form.first_name("Иван")
    form.last_name("Петров")
    form.address("Ленина, 55-3")
    form.e_mail("test@skypro.com")
    form.phone("+7985899998787")
    form.city("Москва")
    form.country("Россия")
    form.job_position("QA")
    form.company("SkyPro")
    form.click_form()
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
