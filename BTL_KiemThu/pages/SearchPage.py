from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.NAME, "query")
        self.result_found = (By.XPATH, "//*[contains(text(),'kết quả tìm kiếm phù hợp')]")
        self.no_result = (By.XPATH, "//*[contains(text(),'Không tìm thấy')]")
        self.product_item = (By.CSS_SELECTOR, "a.product_overlay_action")

    def search_product(self, keyword):
        """Nhập từ khóa và nhấn Enter"""
        search_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.search_box)
        )
        search_input.clear()
        search_input.send_keys(keyword)
        search_input.send_keys(Keys.ENTER)

    def get_search_result(self):
        """Trả về nội dung hiển thị trên trang kết quả tìm kiếm"""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.any_of(
                    EC.presence_of_element_located(self.result_found),
                    EC.presence_of_element_located(self.no_result)
                )
            )
            if self.driver.find_elements(*self.result_found):
                return self.driver.find_element(*self.result_found).text
            elif self.driver.find_elements(*self.no_result):
                return self.driver.find_element(*self.no_result).text
            else:
                return "Không xác định được kết quả tìm kiếm"
        except Exception:
            return "Không xác định được kết quả tìm kiếm"

    def click_first_product(self):
        """Click vào sản phẩm đầu tiên sau khi tìm kiếm"""
        product = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.product_item)
        )
        product_name = product.get_attribute("title") or product.text

        # Cuộn tới sản phẩm để hiển thị
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", product)

        import time
        time.sleep(1)

        self.driver.execute_script("arguments[0].click();", product)
        return product_name
