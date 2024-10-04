from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.metod_calc import Calc_form


def test_calcul():
    driver = webdriver.Chrome()
    form = Calc_form(driver)
    form.delay("45")
    form.click_form()
    WebDriverWait(driver, 46).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))
    result_text = driver.find_element(By.CLASS_NAME, "screen").text
    assert result_text == "15"
    driver.quit()
