import os
import pytest
from selenium import webdriver
from pages.SearchPage import SearchPage
from utils.excel_utils import ExcelUtils
from selenium.webdriver.chrome.options import Options

excel_path = os.path.abspath("data/Data.xlsx")
excel = ExcelUtils(excel_path, sheet_name="Search")
test_data = excel.get_data(mode="search")

@pytest.mark.parametrize("tc_id, keyword, expected", test_data)
def test_search_product(tc_id, keyword, expected):
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    page = SearchPage(driver)
    screenshot_path = ""

    try:
        driver.get("https://rubies.vn/")
        page.search_product(keyword)
        actual = page.get_search_result()
        if str(expected).strip().lower() in str(actual).strip().lower():
            status = "Pass"
        else:
            status = "Fail"
            screenshot_path = ExcelUtils.screenshot(driver, tc_id)

        excel.write_result(tc_id, actual, expected, mode="search", screenshot_path=screenshot_path)

        assert status == "Pass", f"{tc_id} thất bại. Mong đợi: '{expected}', thực tế: '{actual}'"

    finally:
        driver.quit()
