import pytest
import os
from selenium import webdriver
from pages.DangNhap_pages import DangNhapPage
from utils.excel_utils import ExcelUtils
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

excel_path = os.path.abspath("data/Data.xlsx")
excel = ExcelUtils(excel_path, sheet_name="DangNhap")
test_data = excel.get_data(mode="login")  

@pytest.mark.parametrize("id,email,password,expected", test_data)
def test_login_excel(id, email, password, expected):
    driver = webdriver.Chrome()
    driver.set_window_size(1920, 1080)

    try:
        login_page = DangNhapPage(driver)
        login_page.open()
        login_page.login(email, password)

        actual_text = ""

        try:
            message_element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, ".form__message, .errors, .alert")
                )
            )
            actual_text = message_element.text.strip()
        except:
            try:
                title_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.TAG_NAME, "h1"))
                )
                actual_text = title_element.text.strip()
            except:
                actual_text = "Không xác định"

        screenshot_path = ""
        if expected.lower() not in actual_text.lower():  
            screenshot_path = ExcelUtils.screenshot(driver, id)

        excel.write_result(id, actual_text, expected, mode="login", screenshot_path=screenshot_path)

        print(f"Test {id} - Email: {email} - Expected: '{expected}' - Actual: '{actual_text}'")

    finally:
        driver.quit()
