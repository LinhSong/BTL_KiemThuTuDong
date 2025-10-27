import pytest
from selenium import webdriver
from pages.DangKy_pages import DangKyPage
from utils.excel_utils import ExcelUtils
import os

excel_path = os.path.abspath("data/Data.xlsx")
excel = ExcelUtils(excel_path, sheet_name="DangKy")
test_data = excel.get_data(mode="register")

@pytest.mark.parametrize("id,ho,ten,email,sdt,password,expected", test_data)
def test_register_excel(id, ho, ten, email, sdt, password, expected):
    driver = webdriver.Chrome()
    driver.set_window_size(1920, 1080)

    try:
        register_page = DangKyPage(driver)
        register_page.open()
        register_page.register(ho, ten, email, sdt, password)

        # Lấy actual_text bằng hàm error_messages
        actual_text = register_page.error_messages()

        excel.write_result(id, actual_text, expected, mode="register")

        print(f"Test {id} - Email: {email} - Expected: '{expected}' - Actual: '{actual_text}'")
        assert expected.lower() in actual_text.lower(), f"Test {id}: Mong đợi '{expected}', thực tế '{actual_text}'"

    finally:
        driver.quit()
