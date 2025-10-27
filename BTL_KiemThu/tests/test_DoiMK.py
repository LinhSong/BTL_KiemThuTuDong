import os
import pytest
from selenium import webdriver
from pages.DangNhap_pages import DangNhapPage
from pages.DoiMk_pages import DoiMKPage
from utils.excel_utils import ExcelUtils

excel_path = os.path.abspath("data/Data.xlsx")
excel = ExcelUtils(excel_path, sheet_name="DoiMatKhau")
test_data = excel.get_data(mode="DoiMatKhau")

@pytest.mark.parametrize("id,old_pass,new_pass,confirm_pass,expected", test_data)
def test_change_password_excel(id, old_pass, new_pass, confirm_pass, expected):
    driver = webdriver.Chrome()
    driver.set_window_size(1920, 1080)

    try:
        login_page = DangNhapPage(driver)
        login_page.open()
        login_page.login("linhsong1909@gmail.com", "linh@1234")

        change_page = DoiMKPage(driver)
        change_page.open()
        change_page.change_password(old_pass, new_pass, confirm_pass)
        actual_text = change_page.get_message()

        screenshot_path = ""
        if expected not in actual_text:
            screenshot_path = ExcelUtils.screenshot(driver, id)  # chụp màn hình nếu sai

        excel.write_result(id, actual_text, expected, mode="DoiMatKhau", screenshot_path=screenshot_path)

        print(f"Test {id} - Expected: '{expected}' - Actual: '{actual_text}'")
        assert expected.lower() in actual_text.lower(), f"Test {id} failed. Mong đợi '{expected}', thực tế '{actual_text}'"

    finally:
        driver.quit()
