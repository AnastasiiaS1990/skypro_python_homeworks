from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pages.metod_shop import Avtoriz_form
from pages.metod_shop import Shop_form
from pages.metod_shop import Basket_form
from pages.metod_shop import Your_information


def test_shop():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    avtoriz_form = Avtoriz_form(driver)
    avtoriz_form.user_name("standard_user")
    avtoriz_form.password("secret_sauce")
    avtoriz_form.click_form()
    shop_form = Shop_form(driver)
    shop_form.basket()
    basket_form = Basket_form(driver)
    basket_form.checkout()
    your_information = Your_information(driver)
    your_information.first_name("Nastia")
    your_information.last_name("St")
    your_information.postal_code("650405")
    your_information.click_form_info()
    total_price = driver.find_element(By.CSS_SELECTOR, ".summary_total_label")
    total = total_price.text.strip().replace("Total: $", "")
    expected_total = "58.29"
    assert total == expected_total
    driver.quit()
