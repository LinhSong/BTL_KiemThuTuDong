import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.SearchPage import SearchPage
from pages.CartPage import CartPage
from utils.excel_utils import ExcelUtils

excel_path = os.path.abspath("data/Data.xlsx")
excel = ExcelUtils(excel_path, sheet_name="Cart")
test_data = excel.get_data(mode="search")

@pytest.mark.parametrize("tc_id, keyword, expected", test_data)
def test_add_to_cart(tc_id, keyword, expected):
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    screenshot_path = ""
    try:
        driver.get("https://rubies.vn/")
        search_page = SearchPage(driver)
        cart_page = CartPage(driver)

        search_page.search_product(keyword)
        product_name = search_page.click_first_product()
        cart_page.add_to_cart()

        #  Mở giỏ hàng
        #cart_page.go_to_cart()

        #  Kiểm tra sản phẩm có trong giỏ hàng
        #actual = "Có trong giỏ hàng" if cart_page.is_product_in_cart(product_name) else "Không có trong giỏ hàng"

        # Chụp ảnh nếu sai
       #  if expected not in actual:
         #    screenshot_path = ExcelUtils.screenshot(driver, tc_id)

        # Ghi kết quả ra Excel
        # excel.write_result(tc_id, actual, expected, mode="search", screenshot_path=screenshot_path)

        # So sánh
        # assert expected in actual, f"{tc_id} thất bại. Mong đợi: '{expected}', Thực tế: '{actual}'"

    finally:
        driver.quit()
